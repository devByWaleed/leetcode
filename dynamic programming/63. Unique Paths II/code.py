from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

         # If start or end is obstacle, no paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        # List Comprehension
        # dp = [ [0] * (n + 1) for _ in range(m + 1) ]

        # DP table, (m-1,n-1)th position holds answer
        dp = []
        for _ in range(m):
            dp.append([1] * (n))
            
        # Fill first row (only right moves)
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0

        # Fill first column (only down moves)
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0

        # Looping till (m,n)
        for i in range(1, m):
            for j in range(1, n):
                # Handling Obstacle
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # Previous Row
                    prev_row = dp[i - 1][j]
                    # Previous Column
                    prev_col = dp[i][j - 1]
                    dp[i][j] = prev_row + prev_col

        # Return answer
        return dp[m-1][n-1]


obj = Solution()
print(obj.uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]]))             # 2
print(obj.uniquePathsWithObstacles([[0,1], [0,0]]))             # 1
print(obj.uniquePathsWithObstacles([[1,0]]))             # 0

# T.C: O(M * N)
# S.C: O(M * N)