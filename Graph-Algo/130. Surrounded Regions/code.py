from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Edge case
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        # UP, RIGHT, DOWN, LEFT
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque()

        # PART 1 -- Adding Boundary O's to queue
        for i in range(rows):
            for j in range(cols):
                is_border = (i == 0 or i == rows-1 or j == 0 or j == cols-1)
                if is_border and board[i][j] == "O":
                    queue.append((i, j))
                    # Temporary change
                    board[i][j] = "."

        # PART 2 -- Checking Boundary O's
        while queue:
            # Boundary O's
            curr_row, curr_col = queue.popleft()

            for row_delta, col_delta in directions:
                # All 4 neighbors
                next_row = curr_row + row_delta
                next_col = curr_col + col_delta

                # PART 3 -- Inbound check
                row_check = next_row >= 0 and next_row < rows
                col_check = next_col >= 0 and next_col < cols
                # row_check = (0 <= next_row < rows)
                # col_check = (0 <= next_col < cols)
                if (row_check and col_check and board[next_row][next_col] == "O"):
                    # Temporary change
                    board[next_row][next_col] = "."
                    queue.append((next_row, next_col))

        # PART 4 -- Inplace Change
        for i in range(rows):
            for j in range(cols):
                # Can be changed
                if board[i][j] == "O":
                    board[i][j] = "X"
                # Cannot be changed, restore original
                elif board[i][j] == ".":
                    board[i][j] = "O"

        return board


obj = Solution()
print(obj.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))  
# -> [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
print(obj.solve([["X"]]))  # -> [["X"]]
print(obj.solve([["O","O"],["O","O"]])) # -> [["O","O"],["O","O"]]

# T.C: O(M ∗ N)
# S.C: O(M ∗ N)