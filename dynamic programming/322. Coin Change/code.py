from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


obj = Solution()
print(obj.coinChange([1, 2, 5], 11))            # 3
print(obj.coinChange([2], 3))                   # -1
print(obj.coinChange([1], 0))                   # 0

# T.C: O(N)
# S.C: O(N)