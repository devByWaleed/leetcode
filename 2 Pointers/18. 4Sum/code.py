from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return [[]]

obj = Solution()
print(obj.fourSum([1, 0, -1, 0, -2, 2], 0))     # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(obj.fourSum([2, 2, 2, 2, 2], 8))          # [[2,2,2,2]]