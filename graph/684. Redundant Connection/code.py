from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                # Path compression: make every node point directly to root
                parent[x] = find(parent[x])
            
            # If values matched
            return parent[x]
        
        # Each node has its own parent
        parent = list(range(len(edges)))

        
        for a,b in edges:
            # PARENTS of both nodes
            parent_a, parent_b = find(a-1), find(b-1)

            # If same, cycle detects
            if parent_a == parent_b:
                return [a, b]
            
            # If not, merge sets
            parent[parent_a] = parent_b
            

obj = Solution()
print(obj.findRedundantConnection([[1,2],[1,3],[2,3]]))          # -> [2,3]
print(obj.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # -> [1,4]

# T.C: O(N * A(N))
# S.C: O(N)