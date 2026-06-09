from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        queue = deque()
        time = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        rows, cols = len(grid), len(grid[0])

        # PART 1
        for i in range(rows):
            for j in range(cols):
                curr = grid[i][j]

                # If rotten
                if curr == 2:
                    queue.append((i, j))
                # If fresh
                elif curr == 1:
                    fresh_oranges += 1


        # PART 2
        while queue and fresh_oranges > 0:
            time += 1
            current_level_size = len(queue)

            for _ in range(current_level_size):
                # Rotten orange
                curr_row, curr_col = queue.popleft()

                for row_delta, col_delta in directions:
                    # All 4 neighbors
                    next_row = curr_row + row_delta
                    next_col = curr_col + col_delta

                    # PART 3
                    # Inbound + fresh orange check
                    if (0 <= next_row < rows and 
                        0 <= next_col < cols and
                        grid[next_row][next_col] == 1):
                        grid[next_row][next_col] = 2
                        queue.append((next_row, next_col))
                        fresh_oranges -= 1
                    
                        # If we rott all, return immediately
                        if fresh_oranges == 0:
                            return time
                        
        # Final return
        return -1 if fresh_oranges > 0 else time


obj = Solution()
print(obj.orangesRotting([[2,1,1], [1,1,0], [0,1,1]]))  # -> 4
print(obj.orangesRotting([[2,1,1], [0,1,1], [1,0,1]]))  # -> -1
print(obj.orangesRotting([[0,2]]))  # -> 0

# T.C: O(M ∗ N)
# S.C: O(M ∗ N)