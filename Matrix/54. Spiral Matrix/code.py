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