from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass


obj = Solution()
print(obj.subsetsWithDup([1, 2, 2]))           # [[], [1], [1,2], [1,2,2], [2], [2,2]]
print(obj.subsetsWithDup([0]))                 # [[], [0]]