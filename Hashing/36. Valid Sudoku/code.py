from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidRow(board):
            hash_set = set()
            
            for row in board:
                for col in row:
                    if col == ".":  continue
                    
                    if col in hash_set:
                        return False
                        
                    hash_set.add(col)
                
                hash_set.clear()
            
            return True
        

        def isValidCol(board):
            hash_set = set()
            
            for row in range(0, 9):
                for col in range(0, 9):
                    # board[row][col] is for row, reverse is for column
                    if board[col][row] == ".":  continue
                    
                    if board[col][row] in hash_set:
                        return False
                    
                    hash_set.add(board[col][row])
                
                hash_set.clear()
            
            return True
        

        def isValidGrid(board, row, col):
            hash_set = set()
            
            for i in range(row, row+3):
                for j in range(col, col+3):
                    digit = board[i][j]

                    if digit == ".":    continue
                    
                    if digit in hash_set:
                        return False
                    
                    hash_set.add(digit)

            return True
        

        # Result of checking row
        result1 = isValidRow(board)

        # Result of checking column
        result2 = isValidCol(board)

        # Nested loop for checking grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                result3 = isValidGrid(board, i, j)
                
                if not result3:     return False

        # Final checking of 3 conditions
        return (result1 and result2 and result3)

        
obj = Solution()
print(obj.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))      # True

print(obj.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))      # False

# T.C: O(N ^ 2)
# S.C: O(N)



# Grid Indexing Range:-
'''
1st ==> (0,0) -> (2,2)
2nd ==> (0,3) -> (2,5)
3rd ==> (0,6) -> (2,8)

4th ==> (3,0) -> (5,2)
5th ==> (3,3) -> (5,5)
6th ==> (3,6) -> (5,8)

7th ==> (6,0) -> (8,2)
8th ==> (6,3) -> (8,5)
9th ==> (6,6) -> (8,8)
'''


# Other way of managing functions
'''
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
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))      # True

print(obj.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))      # False

# T.C: O(N ^ 2)
# S.C: O(N)
'''