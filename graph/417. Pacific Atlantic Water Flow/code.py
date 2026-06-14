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
        if m == 1:
            return [[0,0]]

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

# T.C: O(M ∗ N)
# S.C: O(M ∗ N)