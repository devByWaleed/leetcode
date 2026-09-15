# 73. Set Matrix Zeroes

## Problem Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it **in place**.

### Examples

**Example 1:**

```text
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

```

**Example 2:**

```text
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```

### Constraints

* `m == matrix.length`
* `n == matrix[0].length`
* $1 \le m, n \le 200$
* $-2^{31} \le$ `matrix[i][j]` $\le 2^{31} - 1$

### Topics
- Array
- Hash Table
- Matrix

---

### Hint 1
If any cell of the matrix has a zero, we can record its row and column number using additional memory. But if the number of zeroes is large, then we might end up using the same amount of additional memory as the matrix itself.

### Hint 2
Simple improvement uses O(m + n) space, but still not the best solution.

### Hint 3
A great trick would be to use one of the rows and one of the columns to keep track of the zeroes.

### Hint 4
We could use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.
