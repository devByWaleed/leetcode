## 1. LeetCode 283: Move Zeroes

### Pattern: Two Pointers

### Solution 1: Double PASS

```python
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Index where non-zero numbers placed
        write = 0

        # For remaining indices
        read = 0

        for i in range(n):
            # If number is non-zero, assign it to start of array
            if nums[i] != 0:
                nums[write] = nums[i]
                # Help to assign numbers sequentially
                write += 1

            read = write

        # Assign 0 to remaining indices
        for j in range(read, n):
            nums[j] = 0

        return nums


obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]
print(obj.moveZeroes([1, 0]))               # [1, 0]

# T.C:  O(N)    --> Loop through N numbers
# S.C:  O(1)    --> No extra space use
```

### Solution 2: Single PASS
```python
from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Index where non-zero number placed
        slow = 0

        for fast in range(n):
            # If zero, ignore
            if nums[fast] == 0:
                continue
            else:
                # Prevents un-necessary swapping
                if slow != fast:
                    # 1 liner swap
                    '''
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    '''
                    # Swapping using temp
                    temp = nums[fast]
                    nums[fast] = nums[slow]
                    nums[slow] = temp

                # Increment position
                slow += 1

        return nums


obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]
print(obj.moveZeroes([1, 0]))               # [1, 0]

# T.C:  O(N)    --> Loop through N numbers
# S.C:  O(1)    --> No extra space use
```


## 2. LeetCode 459: Repeated Substring Pattern

### Pattern: String matching / Knuth-Morris-Pratt (KMP) algorithm

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # Stores longest prefix suffix length for each element of string
        lps = [0] * n

        # Track previous
        prev_lps = 0
        i = 1

        while i < n:
            # If char matched
            if s[i] == s[prev_lps]:
                # Increment length
                prev_lps += 1
                # Update longest length
                lps[i] = prev_lps
                # Move to next element
                i += 1
            # If not matched
            else:
                # Not negative
                if prev_lps > 0:
                    prev_lps = lps[prev_lps - 1]
                # If 0, then update array with 0
                elif prev_lps == 0:
                    lps[i] = 0
                    # Move to next element
                    i += 1

        # Longest prefix suffix length of s
        L = lps[n-1]

        # Condition 1: string is not empty
        cond1 = L > 0

        # Condition 2: Even length
        cond2 = n % (n-L)

        # MOD return 0 (Falsy), so use not
        return cond1 and not cond2


obj = Solution()
print(obj.repeatedSubstringPattern("abab"))             # True
print(obj.repeatedSubstringPattern("aba"))              # False
print(obj.repeatedSubstringPattern("abcabcabcabc"))     # True

# T.C: O(N)     --> Loop through N elements
# S.C: O(N)     --> lps array of size N
```