## 261. Graph Valid Tree

### Description
Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (where each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

A graph is a valid tree if:
1. It is fully connected (all nodes can reach every other node).
2. It contains no cycles.

### Topic
* Graph
* Depth-First Search (DFS)
* Breadth-First Search (BFS)
* Union-Find (Disjoint Set Union)

### Hints
1. **Edge Count Property:** For a graph with `n` nodes to be a tree, it must have **exactly `n - 1` edges**. Fewer edges leave nodes disconnected; more edges guarantee a cycle.
2. **Connectivity:** Starting from node `0`, perform a traversal (DFS or BFS) to visit all reachable nodes. If the count of visited nodes equals `n`, the graph is connected.
3. **Cycle Detection with Union-Find:** Iterate through each edge and union the nodes. If two nodes are already in the same set before merging, a cycle is present.

### Test Cases

#### Test Case 1
* **Input:** `n = 5`, `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`
* **Output:** `true`

#### Test Case 2
* **Input:** `n = 5`, `edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`
* **Output:** `false`

#### Test Case 3
* **Input:** `n = 4`, `edges = [[0, 1], [2, 3]]`
* **Output:** `false`

### Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **DFS / BFS** | $O(V + E)$ or $O(n)$ | $O(V + E)$ or $O(n)$ |
| **Union-Find** | $O(n \cdot \alpha(n))$ | $O(n)$ |