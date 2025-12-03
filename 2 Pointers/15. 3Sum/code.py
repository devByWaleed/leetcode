from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        
        result = []
        
        # Setting 1st pointer
        for i in range(0, n-2):
            # Skipping duplicates for i
            if i > 0 and nums[i] == nums[i-1]:    continue
            
            # Assignment 2 pointers
            j = i + 1
            k = n - 1
            
            while j < k:
                total = (nums[i] + nums[j] + nums[k])
                
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # Skipping duplicates
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    # If pair found, move both pointers
                    j += 1
                    k -= 1
                    
                # If total is smaller, move left one
                elif total < 0:
                    j += 1
                # Else move right one
                else:
                    k -= 1
                    
        return result


obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))    # [[-1, -1, 2],[-1, 0, 1]]
print(obj.threeSum([0, 1, 1]))                # []
print(obj.threeSum([0, 0, 0]))                # [[0, 0, 0]]

# T.C: O(N ^ 2) 
# S.C: O(1)



# Slightly different approach
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        n = len(nums)

        nums.sort()     # Necessary for pointers approach


        for i in range(0, n-2):

            if(i > 0 and nums[i] == nums[i-1]): continue

            # left pointer right after i
            left = i + 1
            right = n - 1       # right pointer at end of array

            target = -nums[i]

            while left < right:

                # Calculating sum
                total = nums[left] + nums[right]

                # If same, add to result array
                if total == target:
                    
                    result.append([nums[i], nums[left], nums[right]])

                    # Condition for same numbers
                    # while left < right and nums[left] == nums[left+1]:
                    #     left += 1
                    # while left < right and nums[right] == nums[right-1]:
                    #     right -= 1

                    # Moving the pointers
                    left += 1
                    right -= 1

                # Conditions for greater and less sum
                elif total > target:
                    right -= 1
                else:
                    left += 1

            # while nums[i] == nums[i+1] and i < n-2:
            #     i += 1

        return result
        

obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))    # [[-1, -1, 2],[-1, 0, 1]]
print(obj.threeSum([0, 1, 1]))                # []
print(obj.threeSum([0, 0, 0]))                # [[0, 0, 0]]

# T.C: O(N ^ 2) 
# S.C: O(1)
'''