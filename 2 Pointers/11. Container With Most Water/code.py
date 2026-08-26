from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        # calculating total water
        max_water = 0

        # 2 pointers
        left, right = 0, n - 1

        # Condition
        while left <= right:
            # Calculating total water
            # Minimum bcz we can store the water upto the minimum bar
            area = (right - left) * min(height[left], height[right])

            # Update with maximum
            max_water = max(area, max_water)

            # Move pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return max_water


obj = Solution()
print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(obj.maxArea([1, 1]))                       # Output: 1

# T.C: O(N)     --> Loop on N numbers
# S.C: O(1)     --> No data structure usued