from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass        


obj = Solution()
print(obj.combinationSum([2, 3, 6, 7], 7))              # [[2,2,3],[7]]
print(obj.combinationSum([2, 3, 5], 8))                 # [[2,2,2,2],[2,3,3],[3,5]]
print(obj.combinationSum([2], 1))                       # []