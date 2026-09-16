# Blind 75 Part 4: Linked List

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

## 3. LeetCode 48: Rotate Image (Medium)

* **Identified Pattern Upfront:** Matrix / Math
* **Time Taken:** 24 minutes
* **Solution Folder:** [`../../Matrix/48.%20Rotate%20Image/`](../../Matrix/48.%20Rotate%20Image/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/rotate-image/submissions/2143310476)

### Code Solution

```python
from typing import List

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 1: Transposing the matrix
        for i in range(n):
            for j in range(i+1,n):
                # Swapping rows and cols numbers
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2: Reflecting
        for i in range(n):
            # Just 1 operation
            for j in range(n // 2):
                # 1st & last col number swapping
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

        return matrix


obj = Solution()
print(obj.rotate([[1,2,3],[4,5,6],[7,8,9]]))        # [[7,4,1],[8,5,2],[9,6,3]]
print(obj.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))     # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# T.C: O(N ^ 2) --> Nested looping on matrix
# S.C: O(1)     --> No data structure used
```

---

## 4. LeetCode 79: Word Search (Hard)

* **Identified Pattern Upfront:** Backtracking / DFS
* **Time Taken:**  minutes
* **Solution Folder:** [`../../Backtrack/79.%20Word%20Search/`](../../Backtrack/79.%20Word%20Search/)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, index):
            # Word found
            if index == len(word):
                return True

            # "Out of bound" / "Different chars" / "Visited"
            if (i < 0 or j < 0 or i >= m or j >= n) or (board[i][j] != word[index]) or (board[i][j] == "#"):
                return False

            # Storing in temporary place
            temp = board[i][j]

            # Mark as visited
            board[i][j] = "#"

            # Check all 4 directions: DOWN or UP or RIGHT or LEFT
            ans = backtrack(i+1,j,index+1) or backtrack(i-1,j,index+1) or backtrack(i,j+1,index+1) or backtrack(i,j-1,index+1)

            # UNDO: Remark original value
            board[i][j] = temp

            return ans

        # traversing through the board
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    # Complete word found
                    return True

        return False

        
obj = Solution()

# Example 1
board1 = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
print(obj.exist(board1, "ABCCED"))  # True

# Example 2
board2 = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
print(obj.exist(board2, "SEE"))     # True

# Example 3
board3 = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
print(obj.exist(board3, "ABCB"))    # False

# T.C: O(M ∗ N ∗ 4^L)       --> Nested looping on board + checking 4 directions
# S.C: O(L)                 --> Recursive call stack used “Length of word”
```