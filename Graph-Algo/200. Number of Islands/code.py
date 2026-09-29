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