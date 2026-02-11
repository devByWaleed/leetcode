from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Pointers for binary search
        left = 0
        right = len(nums) - 1

        while left < right:
            # Calculate mid
            ''' mid = (left + right) // 2 '''
            mid = left + (right - left) // 2

            # If mid is greater, minimum must be on right side
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # If less, minimum must be on left side 
            else:
                right = mid
        
        # Left pointer will contain minimum
        return nums[left]


obj = Solution()
print(obj.findMin([3, 4, 5, 1, 2]))              # 1
print(obj.findMin([4, 5, 6, 7, 0, 1, 2]))        # 0
print(obj.findMin([11, 13, 15, 17]))             # 11

# T.C: O(LOG N)
# S.C: O(1)