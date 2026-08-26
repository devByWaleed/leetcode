# ⏱️ Part 2: Timed Mock Exam

This document records the results of 4 unseen LeetCode problems attempted under a strict **35-minute timer per problem**. Pattern recognition was explicitly declared upfront prior to coding.

---

## 📌 Performance Summary

| Problem | Difficulty | Identified Pattern Upfront | Time Limit | Time Taken | Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [292. Nim Game](https://leetcode.com/problems/nim-game/submissions/) | Easy | Game Theory / Modular Arithmetic | 35 mins | 34 mins | ✅ Passed |
| [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/submissions/) | Easy | Prefix Sum | 35 mins | 28 mins | ✅ Passed |
| [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/submissions/) | Medium | Prefix Sum + Hash Map | 35 mins | 17 mins | ✅ Passed |
| [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/submissions/) | Medium | Two Pointers (Inward Convergence) | 35 mins | 17 mins | ✅ Passed |

---

## 1. LeetCode 292: Nim Game (Easy)

* **Identified Pattern Upfront:** Game Theory / Modular Math
* **Time Taken:** 34 minutes

### Code Solution

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        stones = n

        # Your turn
        remainder = stones % 4
        
        # If stones are multiple of 4, no chance to win
        if remainder == 0:
            return False
        
        # Removing stones
        stones -= remainder

        # If You remove last stone
        if stones == 0:
            return True
        
        # If n is a multiple of 4, that means opponent fwill fall into the trap.
        return True


obj = Solution()
print(obj.canWinNim(4))  # Output: False
print(obj.canWinNim(1))  # Output: True
print(obj.canWinNim(2))  # Output: True
print(obj.canWinNim(5))  # Output: True


'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        # If stones are multiple of 4, no chance to win
        return n % 4 != 0
            

obj = Solution()
print(obj.canWinNim(4))  # Output: False
print(obj.canWinNim(1))  # Output: True
print(obj.canWinNim(2))  # Output: True
print(obj.canWinNim(5))  # Output: True
'''



# Logically correct, but TLE
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        stones = n

        def removing_stone(stones):
            remainder = stones % 4

            # Some chances to win, so remove 1 stone
            if remainder == 0:
                return 1
            # Opponent will fall in multiple of 4 trap
            else:
                return remainder


        while stones > 0:
            player = removing_stone(stones)
            stones = stones - player

            # If Player remove last stone
            if stones == 0:
                return True
            
            friend = removing_stone(stones)
            stones = stones - friend

            # If Friend remove last stone
            if stones == 0:
                return False
            

obj = Solution()
print(obj.canWinNim(4))  # Output: False
print(obj.canWinNim(1))  # Output: True
print(obj.canWinNim(2))  # Output: True
print(obj.canWinNim(5))  # Output: True
'''
```

---

## 2. LeetCode 724: Find Pivot Index (Easy)

* **Identified Pattern Upfront:** Prefix Sum

* **Time Taken:** 28 minutes

### Code Solution

```python
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        sum_left = [0] * n
        sum_right = [0] * n

        # Leftmost sum for index i
        for i in range(1, n):
            sum_left[i] = sum_left[i-1] + nums[i-1]

        # Rightmost sum for index i
        for j in range(n-2, -1, -1):
            sum_right[j] = sum_right[j+1] + nums[j+1]

        for k in range(n):
            # Find same sum, find pivot index
            if sum_left[k] == sum_right[k]:
                return k

        # No pivot index found
        return -1
    

obj = Solution()
print(obj.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(obj.pivotIndex([1, 2, 3]))           # Output: -1
print(obj.pivotIndex([2, 1, -1]))          # Output: 0

# T.C: O(N)     --> Loop on N times
# S.C: O(N)     --> N size arrays used
```

---

## 3. LeetCode 560: Subarray Sum Equals k (Medium)

* **Identified Pattern Upfront:** Prefix Sum

* **Time Taken:** 17 minutes

### Code Solution

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Map to store prefix sums and their frequencies.
        frequency = {0: 1}

        # Final answer: Total subarrays
        subarray_count = 0

        # Running cumulative prefix sum
        current_sum = 0

        for i in range(n):
            # Add current window sum
            current_sum += nums[i]

            # If we found (current_sum - k), we found the subarray
            if current_sum - k in frequency:
                subarray_count += 1

            # Update the frequency of the current prefix sum
            frequency[current_sum] = frequency.get(current_sum, 0) + 1

        return subarray_count
    

obj = Solution()
print(obj.subarraySum([1, 1, 1], 2))  # Output: 2
print(obj.subarraySum([1, 2, 3], 3))  # Output: 2

# T.C: O(N)     --> Loop on N numbers
# S.C: O(N)     --> N numbers in HashMap
```

---

## 4. LeetCode 11: Container With Most Water (Medium)

* **Identified Pattern Upfront:** Two Pointers

* **Time Taken:** 15 minutes

### Code Solution

```python
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
```

---