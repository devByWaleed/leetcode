# 15: 3Sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        n = len(nums)

        nums.sort()     # Necessary for pointers approach


        for i in range(0, n-2):

            if(i > 0 and nums[i] == nums[i-1]): continue

            left = i + 1
            right = n - 1

            target = -nums[i]

            while left < right:

                total = nums[left] + nums[right]

                if total == target:
                    
                    result.append([nums[i], nums[left], nums[right]])

                    # while left < right and nums[left] == nums[left+1]:
                    #     left += 1
                    # while left < right and nums[right] == nums[right-1]:
                    #     right -= 1

                    left += 1
                    right -= 1

                elif total > target:
                    right -= 1
                else:
                    left += 1

            # while nums[i] == nums[i+1] and i < n-2:
            #     i += 1

        return result
        

obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))       # [[-1, -1, 2],[-1, 0, 1]]
print(obj.threeSum([0, 1, 1]))                # []
print(obj.threeSum([0, 0, 0]))                # [[0, 0, 0]]

# T.C: O(N ^ 2) 
# S.C: O(1)
