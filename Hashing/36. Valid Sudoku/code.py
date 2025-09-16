from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = 9       # Length of rows/columns

        def isValidRow(board, row):

            # hash_set to check the element existance
            hash_set = set()

            # We have row number, so looping on columns (j)
            for j in range(n):

                digit = board[row][j]

                # Skipping the in-valid, according to rules
                if digit == ".":
                    continue

                # If value is in hash_set, the sudoku is in-valid
                if digit in hash_set:
                    return False

                # Adding the digit to kepp track
                hash_set.add(digit)

            return True
        


        def isValidColumn(board, col):

            # hash_set to check the element existance
            hash_set = set()

            # We have column number, so looping on rows (i)
            for i in range(n):

                digit = board[i][col]

                # Skipping the in-valid, according to rules
                if digit == ".":
                    continue

                # If value is in hash_set, the sudoku is in-valid
                if digit in hash_set:
                    return False
   
                # Adding the digit to kepp track
                hash_set.add(digit)

            return True
        

        
        def isValidGrid(board, row, col):
            
            # hash_set to check the element existance
            hash_set = set()

            # Condition in loop for only sub-grid
            for i in range(row, row+3, 1):
                
                for j in range(col, col+3, 1):
                    
                    digit = board[i][j]

                    # Skipping the in-valid, according to rules
                    if digit == ".":
                        continue

                    # If value is in hash_set, the sudoku is in-valid
                    if digit in hash_set:
                        return False

                    # Adding the digit to kepp track
                    hash_set.add(digit)
            
            return True
        

        

        # Loop for checking rows are valid or not
        for i in range(0, n):
            if not isValidRow(board, i):
                return False
            
        # Loop for checking columns are valid or not
        for j in range(0, n):
            if not isValidColumn(board, j):
                return False
            

        # Loop for checking 3x3 sub-grid is valid or not
        
        # Incrementing by 3 for jumping towards the grid, not a single cell
        for i in range(0, n, 3):
            
            for j in range(0, n, 3):
                
                if not isValidGrid(board, i, j):
                    return False
        
            
        # Finally After checking all rows, columns & sub-grid return True (valid sudoku)
        return True



obj = Solution()
print(obj.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
))      # True
print(obj.isValidSudoku(
    [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
))      # False

# T.C: O(N ^ 2)
# S.C: O(N)