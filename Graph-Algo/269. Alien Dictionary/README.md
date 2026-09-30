## 269. Alien Dictionary

### Description
There is a new alien language that uses the Latin alphabet. However, the order among the letters is unknown to you. You are given a list of non-empty words from the alien language's dictionary, where the words are **sorted lexicographically** according to the rules of this new language.

Derive the order of letters in this language. If the order is invalid (e.g., due to cycles or invalid prefixes), return `""`. If there are multiple valid orderings, return any one of them.

### Topic
* Graph
* Topological Sort
* Breadth-First Search (BFS / Kahn's Algorithm)
* Depth-First Search (DFS)

### Hints
1. **Dependency Graph:** Compare adjacent words pair-by-pair (`words[i]` and `words[i + 1]`). The first character position where they differ gives a directed edge: `char1 -> char2`.
2. **Invalid Prefix Edge Case:** If a longer word appears before its prefix (e.g., `"apple"` comes before `"app"`), the dictionary order is invalid $\rightarrow$ return `""`.
3. **Topological Sort:** Process nodes with `in_degree == 0` using BFS (Kahn's Algorithm). If the final ordered list does not contain all unique characters, a cycle exists $\rightarrow$ return `""`.

### Test Cases

#### Test Case 1
* **Input:** `words = ["wrt", "wrf", "er", "ett", "rftt"]`
* **Output:** `"wertf"`

#### Test Case 2
* **Input:** `words = ["z", "x"]`
* **Output:** `"zx"`

#### Test Case 3
* **Input:** `words = ["z", "x", "z"]`
* **Output:** `""` *(Cycle detected: 'z' < 'x' and 'x' < 'z')*

#### Test Case 4
* **Input:** `words = ["abc", "ab"]`
* **Output:** `""` *(Invalid prefix ordering)*

### Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Topological Sort (Kahn's BFS / DFS)** | $O(C)$ | $O(U + E) = O(1)$ |

*(Where $C$ is the total number of characters across all words, $U$ is the number of unique characters ($\le 26$), and $E$ is the number of precedence rules ($\le 26^2$)).*