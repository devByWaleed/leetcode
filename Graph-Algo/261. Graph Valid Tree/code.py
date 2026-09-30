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