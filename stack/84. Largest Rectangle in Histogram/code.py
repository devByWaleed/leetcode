from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # Store maximum area of histogram
        max_area = 0
        
        stack = []
        
        for i, height in enumerate(heights):
          # Extended index
          start = i
          
          while stack and height < stack[-1][0]:
            # Pop current height from stack
            h, j = stack.pop()
            
            # Calculating width & area
            w = i - j
            a = w * h
            
            # Updating area
            max_area = max(max_area, a)
            
            # Update the extended index
            start = j
          
          # Add index and value in stack
          stack.append((height, start))
        
        '''
        Dealing with stack elements
        '''
        while stack:
          h, j = stack.pop()
          
          # Calculate extended width (imagianry n)
          w = n - j
          
          # Updating area
          max_area = max(max_area, w*h)
        
        
        return max_area


obj = Solution()
print(obj.largestRectangleArea([2, 1, 5, 6, 2, 3]))     # 10
print(obj.largestRectangleArea([2, 4]))                 # 4

# T.C: O(N)
# S.C: O(N)