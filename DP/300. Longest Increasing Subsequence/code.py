from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # DP array for storing LIS
        dp = [1] * n

        # Looping through all numbers
        for i in range(1, n):
            # Looping through previous numbers
            for j in range(i):
                # If previous number is smaller, then ith number can be in LIS.
                if nums[j] < nums[i]:
                    # Compare current number with Potential new length
                    dp[i] = max(dp[i], dp[j]+1)

        # MAX of DP is LIS
        return max(dp)


obj = Solution()


# Test Case 1
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(obj.lengthOfLIS(nums))    # 4


# Test Case 2
nums = [0, 1, 0, 3, 2, 3]
print(obj.lengthOfLIS(nums))    # 4


# Test Case 3
nums = [7, 7, 7, 7, 7, 7, 7]
print(obj.lengthOfLIS(nums))    # 1

# T.C: O(N^2)     --> Nested loop over the array to fill dp
# S.C: O(N)       --> dp array of size N