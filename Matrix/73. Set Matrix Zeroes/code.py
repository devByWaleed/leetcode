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