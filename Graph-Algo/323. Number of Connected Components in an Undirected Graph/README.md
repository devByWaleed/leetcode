# 323. Number of Connected Components in an Undirected Graph

## Description

Given $n$ nodes labeled from $0$ to $n-1$ and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

---

## Recommended Time & Space Complexity

* **Time Complexity:** $O(V + E \cdot \alpha(V))$ where $V$ is the number of vertices ($n$), $E$ is the number of edges, and $\alpha$ is the Inverse Ackermann function (effectively constant time).
* **Space Complexity:** $O(V)$ to store the parent and size tracking data structures for the vertices.

---

## Topics

* Graph
* Union-Find (Disjoint Set Union / DSU)
* Depth-First Search (DFS)
* Breadth-First Search (BFS)

---

## Test Cases

### Example 1

* **Input:** `n = 5`, `edges = [[0, 1], [1, 2], [3, 4]]`
* **Output:** `2`

### Example 2

* **Input:** `n = 5`, `edges = [[0, 1], [1, 2], [2, 3], [3, 4]]`
* **Output:** `1`

### Example 3 (Isolated Nodes)

* **Input:** `n = 4`, `edges = [[0, 1]]`
* **Output:** `3`