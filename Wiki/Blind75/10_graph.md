# Blind 75 Part 10: Graph

This part contains problems related to `Graph`, `Topological-Sort`, `Unoin Find`

`Total Count = 8`

---

## 1. LeetCode 128: Longest Consecutive Sequence (Medium)

* **Identified Pattern Upfront:** Hash-Set / Union-Find
* **Time Taken:** 26 minutes
* **Solution Folder:** [`../../Hashing/128.%20Longest%20Consecutive%20Sequence/`](../../Hashing/128.%20Longest%20Consecutive%20Sequence/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/longest-consecutive-sequence/submissions/2156788533)

### Code Solution

```python
from typing import List

# Using Union find (DSU)
class DynamicDisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def findParent(self, node):
        #  If node is seen for the first time, initialize it
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1

        # Base case: node is its own ultimate parent
        if node == self.parent[node]:
            return node
        
        # Path Compression: point directly to the ultimate parent
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        root_u = self.findParent(u)
        root_v = self.findParent(v)

        # If already in the same component, return the size
        if root_u == root_v:
            return self.size[root_u]

        # Attach smaller tree under the larger tree
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
            return self.size[root_v]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
            return self.size[root_u]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case for empty array
        if not nums:
            return 0
        
        # Edge case for 1 element array
        if len(nums) == 1:
            return 1
        
        # Convert the input list to a set for O(1) lookups and to remove duplicates.
        hash_set = set(nums)

        # Initialize disjoint set
        dsu = DynamicDisjointSet()

        # Store longest consecutive sequence.
        max_longest = 0

        for num in hash_set:
            dsu.findParent(num)

            if num + 1 in hash_set:
                # Unoin by size
                curr_size = dsu.unionBySize(num, num+1)

                max_longest = max(max_longest, curr_size)
            else:
                # This is start of sequence
                max_longest = max(max_longest, 1)

        return max_longest


obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))                   # 4
print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))           # 9
print(obj.longestConsecutive([1, 0, 1, 2]))                             # 3
print(obj.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))      # 7
print(obj.longestConsecutive([1, 2, 0, 1]))                             # 3
print(obj.longestConsecutive([0]))                                      # 1
print(obj.longestConsecutive([0, 0]))                                   # 1
print(obj.longestConsecutive([]))                                       # 0

# T.C: O(Nα(N))     --> Inverse Ackermann function + Looping on N unique numbers
# S.C: O(N)         --> Hashset used for Pointers, sizes, N uniques numbers
```

---

## 2. LeetCode 200: Number of Islands (Medium)

* **Identified Pattern Upfront:** Matrix / Graph
* **Time Taken:** 8 minutes
* **Solution Folder:** [`../../Graph-Algo/200.%20Number%20of%20Islands/`](../../Graph-Algo/200.%20Number%20of%20Islands/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/number-of-islands/submissions/2156809835)

### Code Solution

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # directions = [(0,-1), (0,1), (-1,0), (1,0)]

        def explore(grid, r, c, visited):
            # Edge case: Index checking
            row_inbound = 0 <= r and r < len(grid)
            col_inbound = 0 <= c and c < len(grid[0])

            # Checking Index out of bound
            if not row_inbound or not col_inbound:
                return False

            # If value is water
            if grid[r][c] == "0":
                return False

            # Initialize pos
            pos = f"{r},{c}"

            # If this pos already check
            if pos in visited:
                return False

            # Add to visited
            visited.add(pos)

            # Backtrack for all 4 directions: UP, DOWN, LEFT, RIGHT
            explore(grid, r-1, c, visited)
            explore(grid, r+1, c, visited)
            explore(grid, r, c-1, visited)
            explore(grid, r, c+1, visited)

            return True

        # Set to break infinite loop
        visited = set()

        # Final count of islands
        islands = 0

        # Grid Iteration
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if explore(grid, r, c, visited):
                    islands += 1

        return islands


obj = Solution()
print(obj.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))  # -> 1
print(obj.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))  # -> 3

# T.C: O(M * N)    --> Loop through M * N grid
# S.C: O(M * N)    --> M * N call stack used
```
---

## 3. LeetCode 323: Number of Connected Components in an Undirected Graph (Medium)

* **Identified Pattern Upfront:** Union-Find
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../Graph-Algo/323.%20Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph/`](../../Graph-Algo/323.%20Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph/)
* **Submittion Link:** Submitted on Neetcode

### Code Solution

```python
from typing import List

class DynamicDisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def findParent(self, node):
        #  If node is seen for the first time, initialize it
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1

        # Base case: node is its own ultimate parent
        if node == self.parent[node]:
            return node
        
        # Path Compression: point directly to the ultimate parent
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        root_u = self.findParent(u)
        root_v = self.findParent(v)

        # If already in the same component, return the size
        if root_u == root_v:
            return False

        # Attach smaller tree under the larger tree
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n

        dsu = DynamicDisjointSet()

        for [u, v] in edges:
            # Find parents for both nodes
            root_u = dsu.findParent(u)
            root_v = dsu.findParent(v)

            if root_u != root_v:
                # Union by size
                dsu.unionBySize(u, v)
                # If union successfull, Decrement after connecting
                res -= 1

        return res


obj = Solution()
print(obj.countComponents(5, [[0,1],[1,2],[3,4]]))
print(obj.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))

# T.C: O(N + Eα(N))     --> Inverse Ackermann function + Working on N nodes and E edges
# S.C: O(N + E)         --> Hashset used for Pointers, sizes, N uniques numbers
```

---

## 4. LeetCode 417: Pacific Atlantic Water Flow (Medium)

* **Identified Pattern Upfront:** Graph / DFS
* **Time Taken:**  minutes
* **Solution Folder:** [`../../Graph-Algo/417.%20Pacific%20Atlantic%20Water%20Flow/`](../../Graph-Algo/417.%20Pacific%20Atlantic%20Water%20Flow/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/2156847841)

### Code Solution

```python
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, visited):
            # PART 3: Checking for Water Flow
            while queue:
                curr_row, curr_col = queue.popleft()

                for row_delta, col_delta in directions:
                    # All 4 neighbors
                    next_row = curr_row + row_delta
                    next_col = curr_col + col_delta

                    if (
                        (0 <= next_row < m) and (0 <= next_col < n) and
                        (next_row, next_col) not in visited and
                        heights[next_row][next_col] >= heights[curr_row][curr_col]):
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
                        
        
        m, n = len(heights), len(heights[0])
        # Edge case
        # if m == 1:
            # return [[0,0]]

        # UP, RIGHT, DOWN, LEFT
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        pacific = set()
        atlantic = set()

        pacific_queue, atlantic_queue = deque(), deque()
        
        result = []

        # PART 1: Identify Ocean Boundaries
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                    pacific_queue.append((i, j))
                if i == m-1 or j == n-1:
                    atlantic.add((i, j))
                    atlantic_queue.append((i, j))

        # PART 2
        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)

        # PART 4
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result
    

obj = Solution()
print(obj.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))  
# -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(obj.pacificAtlantic([[1]]))  # -> [[0,0]]
print(obj.pacificAtlantic([[2,1],[1,2]]))  # -> [[0,0],[0,1],[1,0],[1,1]]

# T.C: O(M ∗ N)     --> Nested loop on 2D grid
# S.C: O(M ∗ N)     --> M*N Call Stack used
```

---

## 5. LeetCode 261: Graph Valid Tree (Medium)

* **Identified Pattern Upfront:** Graph
* **Time Taken:** 14 minutes
* **Solution Folder:** [`../../Graph-Algo/261.%20Graph%20Valid%20Tree/`](../../Graph-Algo/261.%20Graph%20Valid%20Tree/)
* **Submittion Link:** Submitted on NeetCode

### Code Solution

```python
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge cases:
        if len(edges) != (n-1):
            return False
        if not edges:
            return True

        visited = set()

        # Building graph as adjacency list
        graph = {}
        for edge in edges:
            [ a, b ] = edge
            # Edge cases
            if a not in graph:  graph[a] = []
            if b not in graph:  graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            visited.add(node)
            # Looking for it's neighbors in visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # DFS from node 0
        dfs(0)

        # If all n nodes are visited, the graph is fully connected
        return len(visited) == n
    

obj = Solution()
print(obj.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))          # True
print(obj.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))    # False

# T.C: O(N)     --> Looping over N nodes
# S.C: O(N)     --> Call-Stack for N nodes used
```

---

## 6. LeetCode 207: Course Schedule (Medium)

* **Identified Pattern Upfront:** Graph
* **Time Taken:**  minutes
* **Solution Folder:** [`../../Graph-Algo/207.%20Course%20Schedule/`](../../Graph-Algo/207.%20Course%20Schedule/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/course-schedule/submissions/2157879598)

### Code Solution

```python
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Number of prerequisites for each course
        in_degree = [0] * numCourses
        # Save neighbors
        adj_list = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            # RULE: must take course bi first if you want to take course ai.
            adj_list[b].append(a)
            # Add pre-requisites
            in_degree[a] += 1

        # Adding courses to queue which are ready to taken
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # No. of courses taken
        processed = 0

        while queue:
            # Increment the TAKEN course
            course = queue.popleft()
            processed += 1

            # Lookup on neighbors
            for neighbor in adj_list[course]:
                # prerequisites requirement finish
                in_degree[neighbor] -= 1

                # If no prerequisite, then neighbor is ready to take
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check that completed all courses
        return processed == numCourses
    

obj = Solution()
print(obj.canFinish(2, [[1,0]]))           # -> True
print(obj.canFinish(2, [[1,0],[0,1]]))     # -> False

# T.C: O(V + E)     --> Looping over Vertices + Edges
# S.C: O(V + E)     --> collection of Vertices, Edges stored
```

---

## 7. LeetCode 133: Clone Graph (Medium)

* **Identified Pattern Upfront:** Graph
* **Time Taken:**  minutes
* **Solution Folder:** [`../../Graph-Algo/133.%20Clone%20Graph/`](../../Graph-Algo/133.%20Clone%20Graph/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/clone-graph/submissions/2157895268)

### Code Solution

```python
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case
        if not node:
            return None
        
        cloned = {}         # Hashmap to clone the graph

        def dfs(node, cloned):
            # If node is cloned, return it
            if node in cloned:
                return cloned[node]
            
            # Cloning & saving new node to Hashmap
            new_node = Node(node.val)
            cloned[node] = new_node

            # Cloning neighbors
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor, cloned))

            return new_node

        # Deep copy node
        return dfs(node, cloned)
    

# ==========================================
# MANUAL GRAPH SETUP
# ==========================================

obj = Solution()

# ------------------------------------------
# TEST CASE 1: Connected Graph with 4 Nodes
# adjList = [[2,4],[1,3],[2,4],[1,3]]
# ------------------------------------------
# 1. Create the independent nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# 2. Manually link neighbors based on the adjacency list
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

# 3. Test your algorithm
cloned_1 = obj.cloneGraph(n1)

# 4. Print statements to verify values and deep copy safety
print("--- TEST CASE 1 ---")
print(f"Original Node 1 Address: {hex(id(n1))} | Cloned Node 1 Address: {hex(id(cloned_1))}")
print(f"Cloned Node 1 Val: {cloned_1.val}")
print(f"Cloned Node 1 Neighbors: {[neighbor.val for neighbor in cloned_1.neighbors]}")
print(f"Cloned Node 2 Neighbors: {[neighbor.val for neighbor in cloned_1.neighbors[0].neighbors]}")


# ------------------------------------------
# TEST CASE 2: Single Isolated Node
# adjList = [[]]
# ------------------------------------------
single_node = Node(1)
single_node.neighbors = []

cloned_2 = obj.cloneGraph(single_node)

print("\n--- TEST CASE 2 ---")
print(f"Original Node Address: {hex(id(single_node))} | Cloned Node Address: {hex(id(cloned_2))}")
print(f"Cloned Node Val: {cloned_2.val}")
print(f"Cloned Node Neighbors: {cloned_2.neighbors}")


# ------------------------------------------
# TEST CASE 3: Empty Graph
# adjList = []
# ------------------------------------------
empty_graph = None

cloned_3 = obj.cloneGraph(empty_graph)

print("\n--- TEST CASE 3 ---")
print(f"Cloned Graph: {cloned_3}")

# T.C: O(V + E)     --> Working on Vertices + Edges
# S.C: O(V)         --> Call-Stack for Vertices used
```

---

## 8. LeetCode 269: Alien Dictionary (Hard)

* **Identified Pattern Upfront:** Graph
* **Time Taken:**  minutes
* **Solution Folder:** [`../../Graph-Algo/269.%20Alien%20Dictionary/`](../../Graph-Algo/269.%20Alien%20Dictionary/)
* **Submittion Link:** Submitted on NeetCode

### Code Solution

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize graph data structures
        # adj maps each character to a set of characters that come after it
        adj = {char: set() for word in words for char in word}
        # in_degree tracks the count of incoming edges for each unique character
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: Build the directed graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Edge Case: Prefix check (e.g., "abcd" comes before "abc")
            # An invalid dictionary where a longer word precedes its prefix
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            # Find the first character where the two words differ
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # word1[j] must come BEFORE word2[j] (edge: word1[j] -> word2[j])
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    # Only the first differing character gives us relative ordering
                    break

        # Step 3: Collect all nodes with 0 in-degree (no predecessors)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        res = []

        # Step 4: Process graph using BFS (Kahn's Algorithm)
        while queue:
            char = queue.popleft()
            res.append(char)

            # Decrease in-degree for all neighboring characters
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add neighbor to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Cycle Check
        # If the ordering includes all unique characters, return it.
        # Otherwise, a cycle was detected (invalid ordering) -> return ""
        if len(res) == len(in_degree):
            return "".join(res)
        else:
            return ""


obj = Solution()
print(obj.foreignDictionary(["z","o"]))                         # "zo"
print(obj.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))   # "hernf"
print(obj.foreignDictionary(["abc","ab"]))                      # ""

# T.C: O(N)     --> Looping over N nodes
# S.C: O(N)     --> Call-Stack for N nodes used
```