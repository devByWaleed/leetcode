from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      # Pointers for binary search
      left = 0
      right = len(nums) - 1
      
      # Runs for last possible element
      while left < right:
        # Calculate mid
        ''' mid = (left + right) // 2 '''
        mid = left + (right - left) // 2
        
        # If found, return the index
        if target == nums[mid]:
          return mid
        
        # If greater, search on right side
        elif target > nums[mid]:
          left = mid + 1
        
        # If smaller, search on left side
        else:
          right = mid - 1
      
      # If not found, return -1
      return -1


obj = Solution()
print(obj.search([-1, 0, 3, 5, 9, 12], 9))    # 4
print(obj.search([-1, 0, 3, 5, 9, 12], 2))    # -1

# T.C: O(LOG N)
# S.C: O(1)