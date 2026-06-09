from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


obj = Solution()
print(obj.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))  
# -> [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
print(obj.solve([["X"]]))  # -> [["X"]]