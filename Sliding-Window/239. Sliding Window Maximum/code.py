from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()    # Track max element in current window
        
        result = []     # Resultant array


        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if window and window[0] < (i - k + 1):
                window.popleft()

            # Maintain decreasing order in deque
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            # Adding current number's index to window
            window.append(i)

            # If current index is maximum, add it to result
            if i >= (k - 1):
                result.append(nums[window[0]])
            

        return result
        

obj = Solution()
print(obj.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))     # [3, 3, 5, 5, 6, 7]
print(obj.maxSlidingWindow([1], 1))                            # [1]

# T.C: O(N)
# S.C: O(K)



# Brute-Force (Finding max in loop)
'''
from typing import List
from collections import windowque

class Solution:
    windowf maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = windowque()
        result = []

        for i in range(k):
            window.append(nums[i])
        
        max_num = max(window)
        result.append(max_num)

        left = 0
        # right = n - 1

        for right in range(k, n):
            window.append(nums[right])

            window.popleft()
            left += 1

            result.append(max(window))

        return result
        

obj = Solution()

print()
print(obj.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))     # [3, 3, 5, 5, 6, 7]
print(obj.maxSlidingWindow([1], 1))                     # [1]
'''