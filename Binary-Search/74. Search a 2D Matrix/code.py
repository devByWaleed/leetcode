from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # Pointers for binary search
        left = 0

        # Points to last element if seen as flatten
        right = (m * n) - 1
        
        # Runs for last possible element
        while left <= right:
            # Calculate mid
            ''' mid = (left + right) // 2 '''
            mid = left + (right - left) // 2

            # How many rows you have passed
            row = mid // n

            # How far you are in current row
            col = mid % n

            # Extract mid element in 2d matrix
            mid_element = matrix[row][col]
            
            # If found, return True
            if target == mid_element:
                return True
            
            # If greater, search on right side
            elif target > mid_element:
                left = mid + 1
            
            # If smaller, search on left side
            else:
                right = mid - 1
        
        # If not found, return False
        return False


obj = Solution()
print(obj.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]], 3))      # True
print(obj.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]], 13))     # False

print("Test 1 (End of m):", obj.searchMatrix([[1, 3, 5, 7]], 7))                 # True
print("Test 2 (Single Element):", obj.searchMatrix([[10]], 10))                    # True
print("Test 3 (Underflow):", obj.searchMatrix([[5, 10], [15, 20]], 1))             # False
print("Test 4 (Overflow):", obj.searchMatrix([[5, 10], [15, 20]], 25))             # False
print("Test 5 (Middle):", obj.searchMatrix([[1, 3, 5], [7, 9, 11]], 9))            # True

# T.C: O(LOG M * N)
# S.C: O(1)





# Brute Force -> O(M * LOG N)
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(nums, target):
            # Pointers for binary search
            left = 0
            right = len(nums) - 1
            
            # Runs for last possible element
            while left <= right:
                # Calculate mid
                ''' mid = (left + right) // 2 '''
                mid = left + (right - left) // 2
                
                # If found, return the index
                if target == mid_element:
                    return True
                
                # If greater, search on right side
                elif target > mid_element:
                    left = mid + 1
                
                # If smaller, search on left side
                else:
                    right = mid - 1
            
            # If not found, return -1
            return False

        is_find = False

        for i in range(len(matrix)):
            if is_find:
                break
            is_find = binary_search(matrix[i], target)

        return is_find


obj = Solution()
print(obj.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]], 3))      # True
print(obj.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 60]], 13))     # False

print("Test 1 (End of m):", obj.searchMatrix([[1, 3, 5, 7]], 7)) 
print("Test 2 (Single Element):", obj.searchMatrix([[10]], 10))
print("Test 3 (Underflow):", obj.searchMatrix([[5, 10], [15, 20]], 1))
print("Test 4 (Overflow):", obj.searchMatrix([[5, 10], [15, 20]], 25))
print("Test 5 (Middle):", obj.searchMatrix([[1, 3, 5], [7, 9, 11]], 9))
"""