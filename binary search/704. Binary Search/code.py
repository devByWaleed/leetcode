from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      # Pointers for binary search
      start = 0
      end = len(nums) - 1
      
      # Runs for last possible element
      while start < end:
        # Calculate mid
        ''' mid = (start + end) // 2 '''
        mid = start + (end - start) // 2
        
        # If found, return the index
        if target == nums[mid]:
          return mid
        
        # If greater, search on right side
        elif target > nums[mid]:
          start = mid + 1
        
        # If smaller, search on left side
        else:
          end = mid - 1
      
      # If not found, return -1
      return -1


obj = Solution()
print(obj.search([-1, 0, 3, 5, 9, 12], 9))    # 4
print(obj.search([-1, 0, 3, 5, 9, 12], 2))    # -1

# T.C: O(LOG N)
# S.C: O(1)