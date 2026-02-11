from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pass


obj = Solution()
print(obj.search([2, 5, 6, 0, 0, 1, 2], 0))              # True
print(obj.search([2, 5, 6, 0, 0, 1, 2], 3))              # False

# T.C: O(LOG N)
# S.C: O(1)