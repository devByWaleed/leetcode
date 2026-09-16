from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, index):
            # Word found
            if index == len(word):
                return True

            # "Out of bound" / "Different chars" / "Visited"
            if (i < 0 or j < 0 or i >= m or j >= n) or (board[i][j] != word[index]) or (board[i][j] == "#"):
                return False

            # Storing in temporary place
            temp = board[i][j]

            # Mark as visited
            board[i][j] = "#"

            # Check all 4 directions: DOWN or UP or RIGHT or LEFT
            ans = backtrack(i+1,j,index+1) or backtrack(i-1,j,index+1) or backtrack(i,j+1,index+1) or backtrack(i,j-1,index+1)

            # UNDO: Remark original value
            board[i][j] = temp

            return ans

        # traversing through the board
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    # Complete word found
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

# T.C: O(M ∗ N ∗ 4^L)       --> Nested looping on board + checking 4 directions
# S.C: O(L)                 --> Recursive call stack used “Length of word”