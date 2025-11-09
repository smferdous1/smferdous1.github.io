---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
use_math: true
---


My research focuses on designing scalable algorithms for large-scale **combinatorial optimization** problems that arise in domains such as **machine learning**, **quantum computing**, **electronic design automation**, and **data center networking**.  
I work in  both theory and practice, where I develop **provably efficient algorithms**—with quality guarantees—that also **scale on high-performance computing systems**. I combine algorithmic models such as **streaming**, **parallel**, and **poly-streaming** to simultaneously achieve memory and runtime efficiency. I summarize my recent research activities and interests here.

---

### 💾 Memory Efficiency through Streaming Algorithm
When solving large-scale problems, **memory requirements** often become the primary bottleneck for performance.  
The *streaming computational model*, proposed in theoretical computer science, tackles this issue by assuming that data items arrive one at a time, and only a small (sublinear) amount of memory is available for processing.

For example, given a graph with $n$ vertices, a streaming—or more precisely, a *semi-streaming*—algorithm is allowed to use only $O(n \log n)$ memory, even though the graph may contain $O(n^2)$ edges. Such algorithms are typically evaluated based on two key metrics: *Approximation guarantee:* the solution quality relative to the optimal, and *Number of passes:* how many times the algorithm scans the input stream. My research in streaming algorithm is centered around designing and implementing efficient algorithms that have theoretically proven quality guarantee and also show superior empiricial performance. I highlight my recent published work in streaming algorithms.


- **Semi-streaming $k$-Disjoint Matching with applicaiton to data center networking [[ESA24]](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.53)**
  - Two single-pass semi-streaming algorithms for the maximum weight $k$-disjoint matching ($k$-DM) problem are developed. 
  - The first algorithm is based on the primal-dual framework of a linear programming relaxation of the problem and is $1/(3+\varepsilon)$-approximate. 
  - Developed an approximation preserving reduction from $k$-DM to the maximum weight $b$-matching problem. Leveraging this reduction and an existing semi-streaming $b$-matching algorithm, we design a $(1/(2+\varepsilon))(1 - 1/(k+1))$-approximate algorithm. 
  - We also provide implementaion of our algorithms and compare against state-of-the-art offline approaches using synthetic and real-world graph. 

- **Semi-streaming algorithms for edge cover [[SEA24]](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2024.12)**
  - Developed and implemented novel streaming algorithms for *minimum weight edge cover (MWC)* problem and benchmark existing streaming matching algorithm comparing against state-of-the-art offline algorithms. 
  - Two algorithms for MWC is proposed: i) a single pass $2$-approximate algorithm, and ii) a two pass $3/2 +\varepsilon$-approximate algorithm.
- **Semi-streaming algorithms for hypergraph matching [[ESA25]](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.79)**
  - Two single pass semi-streaming algorithms for *weighted hypergraph matching* with approximation guarantees: i) $\frac{1}{d(1+\varepsilon)}$ and ii) $\frac{1}{(2d-1) + 2 \sqrt{d(d-1)}}$, where $d$ is the maximum size of a hyperedge. 
  - These algorithms are compared against offline greedy algorithm using extensive dataset.

---
### ⚡ Parallelizing Streaming Algorithms

Streaming algorithms process data sequentially with strict memory constraints. To enable faster computation on large-scale data, my research explores how to combine parallel processing with streaming efficiency, achieving both low memory usage and high runtime performance. The following projects showcase this line of work.

- **Picasso: Memory efficient and GPU parallel graph coloring for efficient measurement in quantum computing [[IPDPS24]](https://ieeexplore.ieee.org/document/10579092)**
  - Quantum algorithms like the Variational Quantum Eigensolver (VQE) require grouping *Pauli strings* for efficient measurement.  
  - We modeled this as a graph coloring problem and created *Picasso*, a GPU-based algorithm that colors graphs with *>1 trillion edges using just 40 GB of memory*. 
  - <span style="color:red">Featured</span> in [[PNNL news]](https://www.pnnl.gov/news-media/scientists-speed-groundwork-essential-quantum-computing), [[Quantum Computing Report]](https://quantumcomputingreport.com/pnnl-develops-picasso-algorithm-to-accelerate-quantum-data-preparation-by-85-percent-using-graph-coloring-and-clique-partitioning/), [[Inside HPC]](https://insidehpc.com/2025/04/sparsification-pnnl-slims-down-data-for-quantum/), [[Quantum Insider]](https://thequantuminsider.com/2025/04/24/scientists-speed-up-the-groundwork-essential-for-quantum-computing/).

- **Poly-streaming Model [[ESA25]](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.17)**
  - The *poly-streaming model* generalizes both paradigms, enabling parallel execution with bounded memory.  
  - We developed the *first poly-streaming algorithm for weighted matching*, achieving both speed and space efficiency.
  - <span style="color:red">Awarded Best Paper.</span>

---

### 📈 Submodular Function Optimization
I have been actively developing scalable algorithms for large-scale maximization problems where the objective functions are submodular.
Unlike matching or coloring, submodular functions are nonlinear set functions that exhibit diminishing marginal returns—informally, adding an element to a larger set yields a smaller marginal gain than adding it to a smaller subset.

Submodular functions play a central role in data science and machine learning, powering applications such as data summarization, influence maximization, and active learning. My research in this area has two complementary goals: i) *Scalability*: Designing efficient algorithms that leverage parallel, distributed, and streaming paradigms to handle massive datasets., and ii) *Applicability*: Applying submodular optimization to real-world problems across domains such load-balance in parallel algorithms, influence maximization, and pandemic planning. Below are selected recent works in this direction.

- **Parallel Submodular b-matching and application in load balancing [[ACDA21]](https://epubs.siam.org/doi/10.1137/1.9781611976830.5)**
  - Novel parallel algorithm with $1/3$-approximation guarantee is developed for submodular $b$-matching problem using *local lazy greedy* approach.
  - The algorithm is applied to enhance load-balancing for block assignement in *distribured memory Fock matrix computation* in the [NWChemEx](https://github.com/NWChemEx/NWChemEx) software.

- **GreedyML: Distributed multi-level submodular maximization [[SEA25]](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2025.19)**
  - Introduces highly memory efficient Multi level accumulation for distributred submodular maximization under cardinality constraints.
  - Provided empiricial evidence of performance comparing to the state-of-the-art distributed memory algorithms.
- **GreediRIS: Distributed Streaming Influence Maximization [[JPDPC25]](https://www.sciencedirect.com/science/article/pii/S0743731525000048)**
  - A new distributed memory algorithm for Influence Maximization problem is provided utilizing streaming accumulation.
  - Significant performance gains demonstrated on *512 compute nodes* (32K cores) of the NERSC Perlmutter supercomputer,.
- **DIMPLES: Distributed Influence Maximization [[ICS25]](https://dl.acm.org/doi/10.1145/3721145.3730414)** 
  - Designed a massively parallel algorithms for influence maximization that scales to *8K nodes on 65K GPUs (Frontier supercomputer)*, aiding *pandemic planning and intervention strategies*.
  - <span style="color:red">Awarded Best Paper.</span>

---
