# Capstone Part 3: 3 Backlog Problems

Re-attempted and successfully cleared 3 backlog problems previously failed or stuck on.

## 1. LeetCode 283: Move Zeroes

### Pattern: Two Pointers
* **Solution Folder:** [`../../Arrays/283.%20Move%20Zeroes/`](../../Arrays/283.%20Move%20Zeroes/)
* **Submittion Link:** https://leetcode.com/problems/move-zeroes/submissions/2121499330

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
* **Submittion Link:** https://leetcode.com/problems/move-zeroes/submissions/2121509193

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
* **Solution Folder:** [`../../strings/459.%20Repeated%20Substring%20Pattern/`](../../strings/459.%20Repeated%20Substring%20Pattern/)
* **Submittion Link:** https://leetcode.com/problems/repeated-substring-pattern/submissions/2121597837

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

---

## 3. LeetCode 200: number of Islands

### Pattern: Graph algorithm / DFS
* **Solution Folder:** [`../../graph/200.%20Number%20of%20Islands/`](../../graph/200.%20Number%20of%20Islands/)
* **Submittion Link:** https://leetcode.com/problems/number-of-islands/submissions/2122615409

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # directions = [(0,-1), (0,1), (-1,0), (1,0)]

        def explore(grid, r, c, visited):
            # Edge case: Index out of range
            row_inbound = 0 <= r and r < len(grid)
            col_inbound = 0 <= c and c < len(grid[0])

            if not row_inbound or not col_inbound:
                return False
            
            # If water, then there is no island
            if grid[r][c] == "0":
                return False

            pos = f"{r},{c}"

            # Already checked
            if pos in visited:
                return False

            # Add to set to keep track
            visited.add(pos)

            # Explore all 4 directions
            explore(grid, r, c-1, visited)      # LEFT
            explore(grid, r, c+1, visited)      # RIGHT
            explore(grid, r-1, c, visited)      # UP
            explore(grid, r+1, c, visited)      # DOWN

            # After exploration, we found Island
            return True

        # Set to break infinite loop
        visited = set()

        # Final count of islands
        islands = 0

        # Grid Iteration
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if explore(grid, r, c, visited):
                    islands += 1

        return islands


obj = Solution()
print(obj.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))  # -> 1
print(obj.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))  # -> 3

# T.C: O(M * N)    --> Loop through M * N grid
# S.C: O(M * N)    --> M * N call stack used
```

---

## 🔍 Honest Retro & Weakest Patterns

### 1. Weakest Patterns Identified

* **Math Patterns / Problems:**
    - Could not figure out how `Math` can play role in solving problems involving numbers only.
    - I lose time figuring out how to retrieve the correct `pattern` / `algorithm`.
* **String Matching:**
    - Recognizing that a problem requires String matching but it becomes difficult to figure out how `HashMap` or any other `Data-Structure` actually optimize the solution.

### 2. Action Plan for Mastery

* **Math Plan:**
  1. I will figure out all the basic `Math` patterns along with some algorithms design to solve `Game Theory` problems with `Maths`/
  2. Then I will solve the exact problem for each `Prefix Sum` pattern.

* **String-Matching Plan:**
  1. I will figure out all the patterns `String Matching` have (`including with HashMap`).
  2. Then I will solve the exact problem for each `String Matching` pattern.