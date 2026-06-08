from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass


obj = Solution()
print(obj.orangesRotting([[2,1,1], [1,1,0], [0,1,1]]))  # -> 4
print(obj.orangesRotting([[2,1,1], [0,1,1], [1,0,1]]))  # -> -1
print(obj.orangesRotting([[0,2]]))  # -> 0