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

# T.C: O(V + E)
# S.C: O(V)