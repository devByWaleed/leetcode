from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Initialize dp table
        dp = [0] * (n + 1)

        # Minimum of previous 2 "total costs"
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        # Return answer for nth number (given)
        return dp[n]


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))                                  # 15
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))          # 6

# T.C: O(N)
# S.C: O(N)