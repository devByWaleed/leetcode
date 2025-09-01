from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # for loop starting from 2nd element as 1st one remains same
        for i in range(1, len(nums)):

            # Updating the element by summing it with previous one
            nums[i] = nums[i] + nums[i-1]

        return nums
        

obj = Solution()
print(obj.runningSum([1,2,3,4]))        # [1, 3, 6, 10]
print(obj.runningSum([1,1,1,1,1]))      # [1, 2, 3, 4, 5]
print(obj.runningSum([3,1,2,10,1]))     # [3, 4, 6, 16, 17]

# T.C = O(N)
# S.C = O(1)