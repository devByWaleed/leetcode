from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # directions = [(0,-1), (0,1), (-1,0), (1,0)]

        def explore(grid, r, c, visited):
            # Edge case: Index out of range
            row_inbound = 0 <= r and r < len(grid)
            col_inbound = 0 <= c and c < len(grid[0])

            if not row_inbound or not col_inbound:
                return False
            
            # If water, then there is no island
            if grid[r][c] == "0":
                return False

            pos = f"{r},{c}"

            # Already checked
            if pos in visited:
                return False

            # Add to set to keep track
            visited.add(pos)

            # Explore all 4 directions
            explore(grid, r, c-1, visited)      # LEFT
            explore(grid, r, c+1, visited)      # RIGHT
            explore(grid, r-1, c, visited)      # UP
            explore(grid, r+1, c, visited)      # DOWN

            # After exploration, we found Island
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