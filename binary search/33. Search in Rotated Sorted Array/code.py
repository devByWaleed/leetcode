from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pass


obj = Solution()
print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))              # 4
print(obj.search([4, 5, 6, 7, 0, 1, 2], 3))              # -1
print(obj.search([-1], 0))                               # -1

# T.C: O(LOG N)
# S.C: O(1)