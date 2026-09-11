from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Pointers for binary search
        left = 0
        right = n - 1

        # Runs for last possible element
        while left <= right:
            # Calculate mid
            ''' mid = (left + right) // 2 '''
            mid = left + (right - left) // 2
            
            # If found, return the index
            if target == nums[mid]:
                return mid

            # If left half is sorted
            elif nums[left] <= nums[mid]:
                # If target lies in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # If target doesn't lie in left, then in right
                else:
                    left = mid + 1

            # If right half is sorted
            else:
                # If target lies in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # If target doesn't lie in right, then in left
                else:
                    right = mid - 1

        # If not found, return -1
        return -1
    

obj = Solution()
print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))              # 4
print(obj.search([4, 5, 6, 7, 0, 1, 2], 3))              # -1
print(obj.search([-1], 0))                               # -1
print(obj.search([5, 1, 3], 3))                          # 2

# T.C: O(LOG N)             --> Binary Search used; dividing boundary into half
# S.C: O(1)                 --> No data structure used