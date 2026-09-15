# Blind 75 Part 2: Linked List

This part contains problems related to `Matrix`

`Total Count = 4`

---

## 1. LeetCode 73: Set Matrix Zeroes (Difficulty)

* **Identified Pattern Upfront:** Hash-Tables / MTRIX
* **Time Taken:** 14 minutes
* **Solution Folder:** [`../../Matrix/73.%20Set%20Matrix%20Zeroes/`](../../Matrix/73.%20Set%20Matrix%20Zeroes/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/set-matrix-zeroes/submissions/2142250536)

### Code Solution

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])

        # Sets to track indices where 0 placed
        row_set = set()
        col_set = set()

        # PASS 1: Tracking all 0's
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)

        # PASS 2: Marking rows and cols with 0
        for r in range(m):
            for c in range(n):
                if r in row_set:
                    matrix[r][c] = 0

                if c in col_set:
                    matrix[r][c] = 0
        
        return matrix


obj = Solution()
print(obj.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))         # [[1,0,1],[0,0,0],[1,0,1]]
print(obj.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))   # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# T.C: O(M * N)     --> Nested looping on matrix
# S.C: O(M + N)     --> Size of ROW_SET + COL_SET
```

---

## 2. LeetCode 54: Spiral Matrix (Medium)

* **Identified Pattern Upfront:** Matrix / Simulation
* **Time Taken:** 29 minutes
* **Solution Folder:** [`../../Matrix/54.%20Spiral%20Matrix/`](../../Matrix/54.%20Spiral%20Matrix/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/spiral-matrix/submissions/2142288888)

### Code Solution

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Pointers for boundary tracking
        top, left = 0, 0
        bottom, right = len(matrix)-1, len(matrix[0])-1

        # Final answer array
        result = []

        while top <= bottom and left <= right:
            # 1: Traverse Right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            
            top += 1

            # 2: Traverse Bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # 3: Traverse Left
            if top <= bottom:
                for left_col in range(right, left - 1, -1):
                    result.append(matrix[bottom][left_col])
                bottom -= 1

            # 4: Traverse Top
            if left <= right:
                for top_row in range(bottom, top - 1, -1):
                    result.append(matrix[top_row][left])
                left += 1

        return result


obj = Solution()
print(obj.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))               # [1,2,3,6,9,8,7,4,5]
print(obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))      # [1,2,3,4,8,12,11,10,9,5,6,7]

# T.C: O(M * N)     --> Nested looping on matrix
# S.C: O(1)         --> Max numbers will be 100, still constant
```








---

## 1. LeetCode No.: Name (Difficulty)

* **Identified Pattern Upfront:** 
* **Time Taken:**  minutes
* **Solution Folder:** [`../../`](../../)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
```