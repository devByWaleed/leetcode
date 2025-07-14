from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        n = len(nums)

        # Edge case for invalid pairs
        if n < 4:
            return result
        
        nums.sort()     # Necessary for pointers approach

        # Loop rage for proper indexing of array
        for i in range(0, n-3):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Loop rage for proper indexing of array
            for j in range(i+1, n-2):

                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # left poiter right after the j
                left = j + 1
                right = n - 1       # right pointer at the end

                # 2 pointer condition
                while left < right:

                    # Calculating sum
                    total_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    # If sum matches, add to result array
                    if total_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Condition for same numbers
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        # Moving the poiters
                        left += 1
                        right -= 1
                    
                    # Conditions for greater and less sum
                    elif total_sum > target:
                        right -= 1
                    else:
                        left += 1
        
        return result
 

obj = Solution()
print(obj.fourSum([1, 0, -1, 0, -2, 2], 0))     # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(obj.fourSum([2, 2, 2, 2, 2], 8))          # [[2,2,2,2]]
print(obj.fourSum([0, 0, 0, 0], 0))             # [[0, 0, 0, 0]]

# T.C: O(N ^ 3)
# S.C: O(1)