---
title: "Efficient Weighted Graph Matching on GPUs"
collection: publications
permalink: /publication/2024-11-01-Efficient-Weighted-Graph-Matching-on-GPUs
date: 2024-11-01
venue: 'In the proceedings of SC24: International Conference for High Performance Computing, Networking, Storage and Analysis'
citation: ' Michael Mandulak,  Sayan Ghosh,  S M Ferdous,  Mahantesh Halappanvar,  George Slota, &quot;Efficient Weighted Graph Matching on GPUs.&quot; In the proceedings of SC24: International Conference for High Performance Computing, Networking, Storage and Analysis, 2024.'
abstract: "Weighted matching identifies a maximal subset of edges in a graph such that these edges do not share any vertices in common with each other. As a prototypical graph problem, matching has numerous applications in science and engineering, such as linear algebra, multi-level graph algorithms, computer vision and machine learning. There is a critical need for efficient matching algorithms. However, there are challenges in developing efficient, parallel graph matching methods on contemporary GPGPU systems, due to common complexities in general graph processing, such as irregular memory access patterns and load imbalances. Furthermore, increasingly massive graph sizes and resultant intermediate data commonly exceeds available GPU memory. Although dense-GPU systems are mainstream and offer accelerated on-node interconnection to enhance data access bandwidth, data dependencies and device synchronization costs in multi-GPU enabled massive-graph processing create challenges to sustainable scalability."
paperurl: "/files/pdf/papers/Mandulak et al_Efficient Weighted Graph Matching on GPUs.pdf"
---