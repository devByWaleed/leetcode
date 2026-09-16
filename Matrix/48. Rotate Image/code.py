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