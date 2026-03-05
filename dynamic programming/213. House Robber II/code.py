from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge cases
        if n == 1: return nums[0]

        return max(
            # Exclude 1st house
            self.helper(nums[1:]),
            # Exclude last house
            self.helper(nums[:-1])
        )


    def helper(self, nums):
        # Edge cases
        if len(nums) == 1: return nums[0]
        
        # Initialize dp table
        dp = [0] * (len(nums))

        # Initial cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Maximum b/w left or robbed
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        # Return answer for n-1
        return dp[-1]


obj = Solution()
print(obj.rob([2, 3, 2]))            # 3
print(obj.rob([1, 2, 3, 1]))         # 4
print(obj.rob([1, 2, 3]))            # 3

# T.C: O(N)
# S.C: O(N)