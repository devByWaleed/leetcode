from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        timer = [1] 

        def dfs(node, parent, visited, graph, tin, low, bridges):
            visited[node] = 1
            tin[node] = low[node] = timer[0]
            timer[0] += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if visited[neighbor] == 0:
                    dfs(neighbor, node, visited, graph, tin, low, bridges)
                    
                    # Post-DFS update: Parent takes the minimum low value from the child
                    low[node] = min(low[node], low[neighbor])
                    
                    # Bridge condition check
                    if low[neighbor] > tin[node]:
                        bridges.append([node, neighbor])
                
                else:
                    # Back-edge: Update low using the neighbor's discovery time (tin)
                    low[node] = min(low[node], tin[neighbor])

        # Creating Undirected Graph
        graph = {}
        for edge in connections:
            [ a, b ] = edge
            # Edge cases
            if a not in graph:  graph[a] = []
            if b not in graph:  graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        visited = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []

        dfs(0, -1, visited, graph, tin, low, bridges)

        return bridges


obj = Solution()
print(obj.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))    # [[1,3]] or [[3,1]]
print(obj.criticalConnections(2, [[0,1]]))      # [[0,1]]

# T.C: O(V + E)
# S.C: O(V + E)