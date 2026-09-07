from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge case: Single Element or No-rotation array
        if n == 1 or nums[0] <= nums[n-1]:
            return nums[0]

        # Pointers for binary search
        left = 0
        right = n - 1
        
        # Runs for last possible element
        while left < right:
            # Calculate mid
            ''' mid = (left + right) // 2 '''
            mid = left + (right - left) // 2

            # Un-standard
            '''
            # Right to mid
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]

            # Mid
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            '''
            
            # If mid is greater, minimum must be on right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # If less, minimum must be on left side 
            else:
                right = mid

        # Minimum element
        return nums[left]


obj = Solution()
print(obj.findMin([3, 4, 5, 1, 2]))              # 1
print(obj.findMin([4, 5, 6, 7, 0, 1, 2]))        # 0
print(obj.findMin([11, 13, 15, 17]))             # 11

# T.C: O(LOG N)             --> Binary Search used
# S.C: O(1)                 --> No data structure used