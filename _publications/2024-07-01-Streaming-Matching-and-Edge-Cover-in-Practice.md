---
title: "Streaming Matching and Edge Cover in Practice"
collection: publications
permalink: /publication/2024-07-01-Streaming-Matching-and-Edge-Cover-in-Practice
date: 2024-07-01
venue: 'In the proceedings of LIPIcs, Volume 301, SEA 2024'
link: 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2024.12'
github: 'https://github.com/smferdous1/GraST'
citation: ' S M Ferdous,  Alex Pothen,  Mahantesh Halappanavar, &quot;Streaming Matching and Edge Cover in Practice.&quot; In the proceedings of LIPIcs, Volume 301, SEA 2024, 2024.'
abstract: "Graph algorithms with polynomial space and time requirements often become infeasible for massive graphs with billions of edges or more. State-of-the-art approaches therefore employ approximate serial, parallel, and distributed algorithms to tackle these challenges. However, such approaches require storing the entire graph in memory and thus need access to costly computing resources such as clusters and supercomputers. In this paper, we present practical streaming approaches for solving massive graph problems using limited memory for two prototypical graph problems: maximum weighted matching and minimum weighted edge cover. For matching, we conduct a thorough computational study on two of the semi-streaming algorithms including a recent breakthrough result that achieves a 1/(2 + ε)-approximation of the weight while using O(n log W/ε) memory (here n is the number of vertices and W is the maximum edge weight), designed by Paz and Schwartzman [SODA, 2017]. Empirically, we show that the semi-streaming algorithms produce matchings whose weight is close to the best 1/2-approximate offline algorithm while requiring less time and an order-of-magnitude less memory."
paperurl: "/files/pdf/papers/Ferdous et al_2024_Streaming Matching and Edge Cover in Practice.pdf"
---
