---
title: "Semi-Streaming Algorithms for Weighted k-Disjoint Matchings"
collection: publications
permalink: /publication/2024-09-01-Semi-Streaming-Algorithms-for-Weighted-k-Disjoint-Matchings
date: 2024-09-01
venue: 'In the proceedings of ESA 24: European Symposium on Algorithms'
link: 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.53'
arxiv: 'http://arxiv.org/abs/2311.02073'
citation: ' S. M. Ferdous,  Bhargav Samineni,  Alex Pothen,  Mahantesh Halappanavar,  Bala Krishnamoorthy, &quot;Semi-Streaming Algorithms for Weighted k-Disjoint Matchings.&quot; In the proceedings of ESA 24: European Symposium on Algorithms, 2024.'
abstract: "We design and implement two single-pass semi-streaming algorithms for the maximum weight k-disjoint matching (k-DM) problem. Given an integer k, the k-DM problem is to find k pairwise edge-disjoint matchings such that the sum of the weights of the matchings is maximized. For k ≥ 2, this problem is NP-hard. Our first algorithm is based on the primal-dual framework of a linear programming relaxation of the problem and is 1 -approximate. We also develop an approximation preserving reduction from k-DM 3+ε to the maximum weight b-matching problem. Leveraging this reduction and an existing semi-streaming b-matching algorithm, we design a ( 1 )(1 − 1 )-approximate semi-streaming algorithm for k-DM. For 2+ε k+1 any constant ε > 0, both of these algorithms require O(nk log21+ε n) bits of space. To the best of our knowledge, this is the first study of semi-streaming algorithms for the k-DM problem. We compare our two algorithms to state-of-the-art offline algorithms on 95 real-world and synthetic test problems, including thirteen graphs generated from data center network traces. On these instances, our streaming algorithms used significantly less memory (ranging from 6× to 512× less) and were faster in runtime than the offline algorithms. Our solutions were often within 5% of the best weights from the offline algorithms. We highlight that the existing offline algorithms run out of 1 TB of memory for most of the large instances (> 1 billion edges), whereas our streaming algorithms can solve these problems using only 100 GB memory for k = 8."
paperurl: "/files/pdf/papers/Ferdous et al_2024_Semi-Streaming Algorithms for Weighted k-Disjoint Matchings.pdf"
---
