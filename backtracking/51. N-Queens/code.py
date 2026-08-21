from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Base case: n == 1
        if n == 1:
            return [["Q"]]

        # Stores final answer: n x n board
        result = []
        
        # Stores single pair: Rows with default value
        queen = [["."] * n for _ in range(n)]
        '''
        [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ]
        '''

        def is_safe(row, col):
            # Column checking
            # Row in loop bcz col is a loop variable
            for i in range(row):
                if queen[i][col] == "Q":
                    # It is attack area
                    return False

            # Upper-Left diagonal (row-- , col--)
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if queen[i][j] == "Q":
                    return False

            # Upper-Right diagonal (row-- , col++)
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, +1)):
                if queen[i][j] == "Q":
                    return False

            # No attack at this place
            return True
        

        def backtrack(row):
            # Base case to add into result
            if row == n:
                result.append(["".join(r) for r in queen])
                return

            for col in range(n):
                if is_safe(row, col):
                    # Placing queen
                    queen[row][col] = "Q"

                    # Backtrack: Next row
                    backtrack(row+1)
                    
                    # POP ( UNDO )
                    queen[row][col] = "."
            

        # Call function with initial value
        backtrack(0)
        return result

    
obj = Solution()
print(obj.solveNQueens(4))       # [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
print(obj.solveNQueens(1))       # [["Q"]]

# T.C: O(N!)        --> Number of valid placements explored
# S.C: O(N^2)       --> Recursive call stack used "NxN Matrix"