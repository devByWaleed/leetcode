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
                return True
                
            # Handling duplicates by decreasing search space linearly
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left part is sorted
            elif nums[left] <= nums[mid]:
                # Change the boundary to left of mid
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                
                # Move left to current boundary
                else:
                    left = mid + 1


            # Right part is sorted
            else:
                # Change the boundary to right of mid
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                
                # Move right to current boundary
                else:
                    right = mid - 1

            
        # If not found
        return False


obj = Solution()
print(obj.search([2, 5, 6, 0, 0, 1, 2], 0))              # True
print(obj.search([2, 5, 6, 0, 0, 1, 2], 3))              # False
print(obj.search([1], 0))                                # False

# T.C: O(LOG N)
# S.C: O(1)