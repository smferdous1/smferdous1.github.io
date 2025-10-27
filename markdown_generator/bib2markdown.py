#!/usr/bin/env python3
"""
bib2academicpages.py
--------------------
Convert a .bib file into individual Markdown files for the academicpages (Jekyll/Minimal Mistakes) site.

Usage:
  python3 bib2academicpages.py refs.bib --out _publications

Features:
- Parses common BibTeX entry types without external dependencies
- Builds front matter with: title, collection, date, authors, venue, arxiv/doi/link/paperurl, tags, citation
- Filename format: YYYY-slug.md (falls back to 1900 if year missing)
- Tag parsing from 'keywords' or 'tags' fields
- ArXiv detection from eprint/archivePrefix or arxiv fields

NOTE: This is a lightweight parser intended for typical BibTeX; very exotic formatting may need manual touch-ups.
"""

import argparse, os, re, sys, unicodedata
from datetime import datetime

MONTH_MAP = {
    'jan':'01','january':'01','feb':'02','february':'02','mar':'03','march':'03',
    'apr':'04','april':'04','may':'05','jun':'06','june':'06','jul':'07','july':'07',
    'aug':'08','august':'08','sep':'09','sept':'09','september':'09','oct':'10','october':'10',
    'nov':'11','november':'11','dec':'12','december':'12'
}

def slugify(value):
    value = str(value).strip().lower()
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^a-z0-9]+', '-', value)
    value = re.sub(r'-{2,}', '-', value)
    return value.strip('-') or 'paper'

def clean_val(v):
    if v is None:
        return None
    v = v.strip()
    if (v.startswith('{') and v.endswith('}')) or (v.startswith('"') and v.endswith('"')):
        v = v[1:-1].strip()
    v = re.sub(r'\s+', ' ', v).strip()
    return v

def parse_fields(body):
    fields = {}
    i = 0
    while i < len(body):
        while i < len(body) and body[i] in ' \r\n\t,':
            i += 1
        if i >= len(body):
            break
        m = re.match(r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*', body[i:])
        if not m:
            break
        key = m.group(1).lower()
        i += m.end()
        if i >= len(body):
            break
        if body[i] == '{':
            depth = 0
            j = i
            while j < len(body):
                if body[j] == '{':
                    depth += 1
                elif body[j] == '}':
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                j += 1
            val = body[i:j]
            i = j
        elif body[i] == '"':
            j = i + 1
            while j < len(body):
                if body[j] == '"' and body[j-1] != '\\':
                    j += 1
                    break
                j += 1
            val = body[i:j]
            i = j
        else:
            m2 = re.match(r'([^,]+)', body[i:])
            if m2:
                val = m2.group(1)
                i += m2.end()
            else:
                val = ''
        fields[key] = clean_val(val)
        while i < len(body) and body[i] in ' \r\n\t,':
            if body[i] == ',':
                i += 1
                break
            i += 1
    return fields

ENTRY_RE = re.compile(r'@(\w+)\s*\{\s*([^,]+)\s*,(.*?)\}\s*(?=@|\Z)', re.S)

def parse_bib(text):
    entries = []
    for m in ENTRY_RE.finditer(text):
        entry_type = m.group(1).lower()
        key = m.group(2).strip()
        body = m.group(3)
        fields = parse_fields(body)
        fields['ENTRYTYPE'] = entry_type
        fields['ID'] = key
        entries.append(fields)
    return entries

def first_nonempty(*vals):
    for v in vals:
        if v:
            return v
    return None

def detect_year_month(fields):
    yr = (fields.get('year') or '').strip()
    mo = (fields.get('month') or '').strip().lower()
    mo = mo.strip('{}"\'')
    if mo.isdigit():
        mo = f"{int(mo):02d}"
    else:
        MONTH_MAP_LOCAL = MONTH_MAP
        mo = MONTH_MAP_LOCAL.get(mo, '01') if mo else '01'
    if not yr or not yr.isdigit():
        yr = '1900'
    return yr, mo

def build_citation(f):
    parts = []
    if f.get('author'):
        parts.append(f.get('author'))
    if f.get('title'):
        parts.append(f'"{f.get("title")}"')
    venue = first_nonempty(f.get('booktitle'), f.get('journal'), f.get('venue'))
    if venue:
        parts.append(venue)
    if f.get('year'):
        parts.append(f.get('year'))
    return ', '.join(parts)

def detect_arxiv(f):
    if f.get('arxiv'):
        return f.get('arxiv')
    if f.get('archiveprefix', '').lower() == 'arxiv' and f.get('eprint'):
        return f"https://arxiv.org/abs/{f['eprint']}"
    return None

def detect_link(f):
    doi = f.get('doi')
    if doi:
        doi = doi.strip()
        if doi.lower().startswith('http'):
            return doi
        return 'https://doi.org/' + doi
    return f.get('url')

def detect_pdf(f):
    for k in ('pdf','paper','file','files'):
        v = f.get(k)
        if v and '.pdf' in v.lower():
            import re as _re
            m = _re.search(r'(?P<path>[^:;]+\.pdf)', v, _re.I)
            return m.group('path') if m else v
    url = f.get('url','')
    if url and url.lower().endswith('.pdf'):
        return url
    return None

def main():
    import argparse, sys, os, re
    ap = argparse.ArgumentParser()
    ap.add_argument('bib', help='Path to BibTeX file')
    ap.add_argument('--out', default='_publications', help='Output folder (default: _publications)')
    args = ap.parse_args()

    if not os.path.exists(args.bib):
        sys.exit(f"File not found: {args.bib}")

    os.makedirs(args.out, exist_ok=True)
    text = open(args.bib, 'r', encoding='utf-8', errors='ignore').read()

    # remove lines that begin with %
    lines = [ln for ln in text.splitlines() if not ln.strip().startswith('%')]
    text = '\n'.join(lines)

    entries = parse_bib(text)
    if not entries:
        print("No entries parsed. Check your .bib formatting.")
        return

    count = 0
    for f in entries:
        title = first_nonempty(f.get('title'), f.get('booktitle'), f.get('journal'), f.get('ID')) or 'Untitled'
        # strip braces and quotes often present in BibTeX titles
        import re as _re
        title_stripped = _re.sub(r'[{}"]', '', title).strip()

        year, month = detect_year_month(f)
        day = '01'
        date_iso = f"{year}-{month}-{day}"

        slug = slugify(title_stripped)[:80]
        filename = f"{year}-{slug}.md"
        outpath = os.path.join(args.out, filename)

        authors = first_nonempty(f.get('authors'), f.get('author'))
        venue = first_nonempty(f.get('booktitle'), f.get('journal'), f.get('venue'))
        citation = build_citation(f)
        arxiv = detect_arxiv(f)
        link = detect_link(f)
        pdf = detect_pdf(f)

        raw_kw = first_nonempty(f.get('keywords'), f.get('tags'))
        tags = []
        if raw_kw:
            for t in re.split(r'[;,]', raw_kw):
                t = t.strip()
                if t:
                    tags.append(t)

        front_matter = []
        front_matter.append('---')
        safe_title = title_stripped.replace('"', "'")  # convert inner quotes to single quotes
        front_matter.append(f'title: "{safe_title}"')
        front_matter.append('collection: publications')
        front_matter.append(f'date: {date_iso}')
        if authors:
            front_matter.append(f'authors: "{authors}"')
        if venue:
            front_matter.append(f'venue: "{venue}"')
        if pdf:
            front_matter.append(f'paperurl: "{pdf}"')
        if arxiv:
            front_matter.append(f'arxiv: "{arxiv}"')
        if link:
            front_matter.append(f'link: "{link}"')
        if tags:
            fm_tags = '[' + ', '.join([t for t in tags]) + ']'
            front_matter.append(f'tags: {fm_tags}')
        front_matter.append('---\n')

        body = []
        if 'abstract' in f and f['abstract']:
            body.append(f'**Abstract.** {f["abstract"]}\n')
        if citation:
            body.append(f'*Citation:* {citation}\n')

        with open(outpath, 'w', encoding='utf-8') as w:
            w.write('\n'.join(front_matter))
            if body:
                w.write('\n'.join(body))
        count += 1

    print(f"Wrote {count} publication files to {args.out}")
    print("Tip: Commit them and rebuild your site.")

if __name__ == '__main__':
    main()
