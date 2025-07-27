from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        operations = 0  # To count no. of operations
        
        # Loop range for not getting out of bound error
        for i in range(0, n - 2):

            if nums[i] == 0:


                # Selecting 3 consecutives elements and flip it
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                
                # increment after flipping numbers or before not matters
                operations += 1

        # Checking for last two elements as loop not check them
        if (nums[n - 1] == 0) or (nums[n - 2] == 0):
            return -1   # Returning -1 as per condition (not possible to change it to 1)
        
        return operations


obj = Solution()
print(obj.minOperations([0, 1, 1, 1, 0, 0]))    # 3
print(obj.minOperations([0, 1, 1, 1]))          # -1