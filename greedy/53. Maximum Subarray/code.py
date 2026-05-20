from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge case
        if n == 1:
            return nums[0]
        
        curr_sum = 0
        max_sum = -float("inf")

        for i in range(n):
            # Adding current number
            curr_sum += nums[i]

            # Updating max
            max_sum = max(max_sum, curr_sum)

            # If current is negative, reset to 0
            if curr_sum < 0:
                curr_sum = 0

        return max_sum


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))     # 6
print(obj.maxSubArray([1]))     # 1
print(obj.maxSubArray([5, 4, -1, 7, 8]))     # 23

# T.C: O(N)
# S.C: O(1)