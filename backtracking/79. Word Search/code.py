from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


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