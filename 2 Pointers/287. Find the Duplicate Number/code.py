from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if not nums:
            return 0

        return 0

obj = Solution()
print(obj.findDuplicate([1,3,4,2,2]))   # 2
print(obj.findDuplicate([3,1,3,4,2]))   # 3
print(obj.findDuplicate([3,3,3,3,3]))   # 3