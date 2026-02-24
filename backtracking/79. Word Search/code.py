from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(i, j, index):
            # Base case
            if index == len(word):
                return True
            
            # If "Out of bound" / "Different char" / "Visited"
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != word[index] or board[i][j] == "#":
                return False
            
            # Store value temporarily 
            temp = board[i][j]

            # Mark as visited
            board[i][j] = "#"

            # Checking for adjacent directions
            ans = backtrack(i+1, j, index+1) or backtrack(i-1, j, index+1) or backtrack(i, j+1, index+1) or backtrack(i, j-1, index+1)

            # UNDO: restore original value
            board[i][j] = temp

            return ans
        

        # Traversing matrix
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False


obj = Solution()

# Example 1
board1 = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
print(obj.exist(board1, "ABCCED"))  # True

# Example 2
board2 = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
print(obj.exist(board2, "SEE"))     # True

# Example 3
board3 = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
print(obj.exist(board3, "ABCB"))    # False

# T.C: O(M ∗ N ∗ 4^L)
# S.C: O(L)