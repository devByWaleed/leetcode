from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass

obj = Solution()
print(obj.findIntersectionValues([2, 3, 2], [1, 2]))                     # [2, 1]
print(obj.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))   # [3, 4]
print(obj.findIntersectionValues([3, 4, 2, 3], [1, 5]))                  # [0, 0]