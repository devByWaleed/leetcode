from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def explore(grid, r, c, visited):
            # Out of bound boundary checks
            row_inbound = 0 <= r and r < len(grid)
            col_inbound = 0 <= c and c < len(grid[0])

            if not row_inbound or not col_inbound:
                return False
            
            # For WATER
            if grid[r][c] == "0":
                return False
            
            # Current position
            pos = f"{r},{c}"

            # BREAK infinite loop 
            if pos in visited:
                return False
            
            visited.add(pos)

            # All 4 DIRECTIONS
            explore(grid, r-1, c, visited)  # UP
            explore(grid, r+1, c, visited)  # DOWN
            explore(grid, r, c-1, visited)  # LEFT
            explore(grid, r, c+1, visited)  # RIGHT

            return True


        visited = set()
        count = 0
        for r in range(0, len(grid), 1):
            for c in range(0, len(grid[0]), 1):
                if explore(grid, r, c, visited):
                    count += 1

        return count
    

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

# T.C: O(M * N)
# S.C: O(M * N)