
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # Variables to keep track of max boundary
        max_left, max_right = 0, 0
        
        trapped_water = 0       # calculating total water

        # 2 pointers
        left, right = 0, n - 1

        # Condition
        while left <= right:

            # For left side
            if max_left < max_right:
                # If space is positive, add it
                water = max_left - height[left]
                if water > 0:
                    trapped_water += water
                
                # Else update variable with current height
                else:
                    max_left = height[left]
                left += 1
            
            # For right side
            else:
                # If space is positive, add it
                water = max_right - height[right]
                if water > 0:
                    trapped_water += water
                
                # Else update variable with current height
                else:
                    max_right = height[right]
                right -= 1
        
        return trapped_water


obj = Solution()
print(obj.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))   # 6     
print(obj.trap([4, 2, 0, 3, 2, 5]))                     # 9

# T.C: O(N)
# S.C: O(1)





'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        trapped_water = 0       # Store total water

        # 2 Pointers
        left = 0
        right = n - 1

        # Variables to track maximum height to left & right side
        max_left, max_right = height[left], height[right]


        while left < right:

            # For calculating the water on left side
            if max_left < max_right:

                left += 1       # Updating bcz we have already check the 1st height, outside the loop

                # If current height is greater, update it. Otherwise Calculate the capacity
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    trapped_water += max_left - height[left]

            
            # For calculating the water on right side
            else:
                
                right -= 1       # Updating bcz we have already check the 1st height, outside the loop

                # If current height is greater, update it. Otherwise Calculate the capacity
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    trapped_water += max_right - height[right]
                

        return trapped_water


obj = Solution()
print(obj.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))   # 6     
print(obj.trap([4, 2, 0, 3, 2, 5]))                     # 9

# T.C: O(N)
# S.C: O(1)
'''