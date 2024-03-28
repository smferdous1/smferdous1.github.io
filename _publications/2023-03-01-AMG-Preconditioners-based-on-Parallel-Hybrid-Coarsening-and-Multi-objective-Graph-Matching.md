---
title: "AMG Preconditioners based on Parallel Hybrid Coarsening and Multi-objective Graph Matching"
collection: publications
permalink: /publication/2023-03-01-AMG-Preconditioners-based-on-Parallel-Hybrid-Coarsening-and-Multi-objective-Graph-Matching
date: 2023-03-01
venue: 'In the proceedings of 2023 31st Euromicro International Conference on Parallel, Distributed and Network-Based Processing (PDP)'
link: 'https://ieeexplore.ieee.org/document/10137155/'
citation: ' Pasqua D&apos;Ambra,  Fabio Durastante,  S M Ferdous,  Salvatore Filippone,  Mahantesh Halappanavar,  Alex Pothen, &quot;AMG Preconditioners based on Parallel Hybrid Coarsening and Multi-objective Graph Matching.&quot; In the proceedings of 2023 31st Euromicro International Conference on Parallel, Distributed and Network-Based Processing (PDP), 2023.'
abstract: "We describe preliminary results from a multi-objective graph matching algorithm, in the coarsening step of an aggregation-based Algebraic MultiGrid (AMG) preconditioner, for solving large and sparse linear systems of equations on high-end parallel computers. We have two objectives. First, we wish to improve the convergence behavior of the AMG method when applied to highly anisotropic problems. Second, we wish to extend the parallel package PSCToolkit to exploit multi-threaded parallelism at the node level on multi-core processors. Our matching proposal balances the need to simultaneously compute high weights and large cardinalities by a new formulation of the weighted matching problem combining both these objectives using a parameter λ . We compute the matching by a parallel 2/3−ε -approximation algorithm for maximum weight matchings. Results with the new matching algorithm show that for a suitable choice of the parameter λ we compute effective preconditioners in the presence of anisotropy, i.e., smaller solve times, setup times, iterations counts, and operator complexity."
paperurl: "/files/pdf/papers/D&apos;Ambra et al_2023_AMG Preconditioners based on Parallel Hybrid Coarsening and Multi-objective.pdf"
---
