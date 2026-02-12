from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass


obj = Solution()
print(obj.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]], 3))      # True
print(obj.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]], 13))     # False