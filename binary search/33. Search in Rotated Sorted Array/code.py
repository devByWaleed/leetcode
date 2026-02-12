from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Pointers for binary search
        left = 0
        right = len(nums) - 1
        
        # Runs for last possible element
        while left <= right:
            # Calculate mid
            ''' mid = (left + right) // 2 '''
            mid = left + (right - left) // 2
            
            # If found, return the index
            if target == nums[mid]:
                return mid
            

            # For left side -> move to right side of mid
            if nums[mid] >= nums[left]:
                
                # Change the boundary to left of mid
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                
                # Move left to current boundary
                else:
                    left = mid + 1
            

            # For right side -> move to left side of mid
            else:
                
                # Change the boundary to right of mid
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                
                # Move right to current boundary
                else:
                    right = mid - 1         
        

        # If not found
        return -1


obj = Solution()
print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))              # 4
print(obj.search([4, 5, 6, 7, 0, 1, 2], 3))              # -1
print(obj.search([-1], 0))                               # -1
print(obj.search([5, 1, 3], 3))                          # 2

# T.C: O(LOG N)
# S.C: O(1)