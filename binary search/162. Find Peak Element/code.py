from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge cases
        if n == 1:
            return 0
        
        # 1st element
        if nums[0] > nums[1]:
            return 0
        
        # Last element
        if nums[n-1] > nums[n-2]:
            return n - 1
        
        # Pointers for binary search
        left = 0
        right = n - 1

        # Runs for last possible element
        while left <= right:
            # Calculate mid
            ''' mid = (left + right) // 2 '''
            mid = left + (right - left) // 2
            
            # If mid is peak
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            # Peak on left side
            elif nums[mid] < nums[mid+1]:
                left = mid + 1

            # Peak on right side
            elif nums[mid] > nums[mid+1]:
                right = mid - 1


obj = Solution()
print(obj.findPeakElement([1, 2, 3, 1]))              # 2
print(obj.findPeakElement([1, 2, 1, 3, 5, 6, 4]))     # 5

# T.C: O(LOG N)
# S.C: O(1)