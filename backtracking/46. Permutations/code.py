from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


obj = Solution()
print(obj.permute([1, 2, 3]))           # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(obj.permute([0, 1]))              # [[0,1], [1,0]]