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