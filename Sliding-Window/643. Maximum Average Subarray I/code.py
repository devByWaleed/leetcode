from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        # For shrinking window
        left = 0

        # Calculate maximum average
        max_avg = 0
        
        max_sum = 0     # Calculate sum of current window

        avg = 0     # Current window average


        # Looping first k elements
        for i in range(0, k):
            max_sum += nums[i]

        avg = max_sum / k   # Average of first k elements
        max_avg = avg


        # Iterating through rest of the array
        for right in range(k, n):
            # Expanding window
            max_sum += nums[right]

            # Shrinking window
            max_sum -= nums[left]
            left += 1

            # Calculate avg and update it
            avg = max_sum / k

            max_avg = max(max_avg, avg)

        return max_avg
    

obj = Solution()
print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))                # 12.75000
print(obj.findMaxAverage([5], 1))                                   # 5.00000
print(obj.findMaxAverage([3, 3, 4, 3, 0], 3))                       # 3.33333
print(obj.findMaxAverage([6, 8, 6, 8, 0, 4, 1, 2, 9, 9], 2))        # 9.00000
print(obj.findMaxAverage([4, 0, 4, 3, 3], 5))                       # 2.80000

# T.C: O(N)
# S.C: O(1)


# 2nd approach
'''
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)

        # Calculating sum of first k elements
        window_sum = sum(nums[:k])

        # max_sum to keep track maximum value
        max_sum = window_sum

        # Loop through remaining window
        for i in range(k, n):

            # At each iteration, we add current value and subtract previous one
            window_sum += nums[i] - nums[i - k]

            # Updating maximum sum
            max_sum = max(max_sum, window_sum)

        # Calculating average of maximum sum (i,e., maximum average)
        average = max_sum / k
        
        return average
    

obj = Solution()
print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))                # 12.75000
print(obj.findMaxAverage([5], 1))                                   # 5.00000
print(obj.findMaxAverage([3, 3, 4, 3, 0], 3))                       # 3.33333
print(obj.findMaxAverage([6, 8, 6, 8, 0, 4, 1, 2, 9, 9], 2))        # 9.00000
print(obj.findMaxAverage([4, 0, 4, 3, 3], 5))                       # 2.80000

# T.C: O(N)
# S.C: O(1)
'''