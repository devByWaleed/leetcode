from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # n x n board
        result = []

        # Current row
        path = [["."] * n for _ in range(n)]


        def is_safe(row, col):
            # Column checking
            for i in range(row):
                if path[i][col] == "Q":
                    return False
                
            # Left upper diagonal (row-- , col--)
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if path[i][j] == "Q":
                    return False
            
            
            # Right upper diagonal (row-- , col++)
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if path[i][j] == "Q":
                    return False
                
            return True


        def backtrack(row, n):
            if row == n:
                result.append(["".join(r) for r in path])
                return
            
            for col in range(n):
                if is_safe(row, col):
                    path[row][col] = "Q"

                    # Backtrack
                    backtrack(row+1, n)

                    # UNDO the step
                    path[row][col] = "."


        # Call bactrack function for 1st number
        backtrack(0, n)

        return result


obj = Solution()
print(obj.solveNQueens(4))       # [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
print(obj.solveNQueens(1))       # [["Q"]]

# T.C: O(N!)
# S.C: O(N^2)