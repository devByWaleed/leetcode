from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones = 0        # To keep track of maximum 1's
        current_one = 0     # To keep track of current 1

        for i in range(len(nums)):

            # If 1 finds, update current_one by 1 (to start the track)
            if nums[i] == 1:
                current_one += 1

            # Reset the current window to 0 (last one is minimum)
            elif nums[i] == 0:
                current_one = 0

            # After each number, update max_ones to find the final window
            if current_one > max_ones:
                max_ones = current_one
        
        return max_ones
    
obj = Solution()
print(obj.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))       # 3
print(obj.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))       # 2

# T.C: O(N)
# S.C: O(1)