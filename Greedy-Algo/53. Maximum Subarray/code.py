from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            # Choice 1: Creating new sub-array
            ch1 = nums[i]

            # Choice 2: Extending current window
            ch2 = curr_sum + nums[i]

            # Maximum of 2 choices
            curr_sum = max(ch1, ch2)
            
            # Updating maximum sub-array sum
            max_sum = max(max_sum, curr_sum)

        return max_sum


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))     # 6
print(obj.maxSubArray([1]))     # 1
print(obj.maxSubArray([5, 4, -1, 7, 8]))     # 23

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> No data structure used