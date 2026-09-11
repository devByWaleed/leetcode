from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def left_bound(nums, target):
            # Pointers for binary search
            left = 0
            right = len(nums) - 1

            # Store index of first occurrence
            index = -1
            
            # Runs for last possible element
            while left <= right:
                # Calculate mid
                ''' mid = (left + right) // 2 '''
                mid = left + (right - left) // 2
                
                # If found, update the index
                if target == nums[mid]:
                    index = mid
                    # keep searching LEFT to find the very first one
                    right = mid - 1
                
                # Target is in right half
                elif target > nums[mid]:
                    left = mid + 1
                
                # Target is in left half
                else:
                    right = mid - 1
            
            return index


        def right_bound(nums, target):
            # Pointers for binary search
            left = 0
            right = len(nums) - 1
            
            # Store index of last occurrence
            index = -1
            
            # Runs for last possible element
            while left <= right:
                # Calculate mid
                ''' mid = (left + right) // 2 '''
                mid = left + (right - left) // 2
                
                # If found, return the index
                if target == nums[mid]:
                    index = mid
                    # keep searching RIGHT to find the very last one
                    left = mid + 1
                
                # Target is in right half
                elif target > nums[mid]:
                    left = mid + 1
                
                # Target is in left half
                else:
                    right = mid - 1
            
            return index
        

        first = left_bound(nums, target)
        last = right_bound(nums, target)
        
        return [first, last]
        

obj = Solution()
print(obj.searchRange([5, 7, 7, 8, 8, 10], 8))        # [3, 4]
print(obj.searchRange([5, 7, 7, 8, 8, 10], 6))        # [-1, -1]

# T.C: O(LOG N)
# S.C: O(1)