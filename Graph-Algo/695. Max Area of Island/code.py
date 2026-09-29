from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def explore(grid, r, c, visited):
            # Out of bound boundary checks
            row_inbound = 0 <= r and r < len(grid)
            col_inbound = 0 <= c and c < len(grid[0])

            if not row_inbound or not col_inbound:
                return 0
            
            # For WATER
            if grid[r][c] == 0:
                return 0
            
            # Current position
            pos = f"{r},{c}"

            # BREAK infinite loop 
            if pos in visited:
                return 0
            
            visited.add(pos)

            size = 1

            # All 4 DIRECTIONS
            size += explore(grid, r-1, c, visited)  # UP
            size += explore(grid, r+1, c, visited)  # DOWN
            size += explore(grid, r, c-1, visited)  # LEFT
            size += explore(grid, r, c+1, visited)  # RIGHT

            return size


        
        visited = set()
        max_size = 0
        for r in range(0, len(grid), 1):
            for c in range(0, len(grid[0]), 1):
                size = explore(grid, r, c, visited)
                
                # Update the minimum island size
                if size > max_size:
                    max_size = size

        return max_size


obj = Solution()
print(obj.maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))  # -> 6
print(obj.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))  # -> 0

# T.C: O(M * N)
# S.C: O(M * N)