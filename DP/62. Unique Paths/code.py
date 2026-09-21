# Recursion
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Base case, stop moment
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


obj = Solution()
print(obj.uniquePaths(3, 7))             # 28
print(obj.uniquePaths(3, 2))             # 3

# T.C: O(2 ^ (M+N))
# S.C: O(M + N)
'''



# Memoization
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memo table
        memo = {}

        def solve(m, n):
            key = f"{m} , {n}"
            # key = (m, n)

            # Lookup in memo for quick result
            if key in memo:
                return memo[key]
            
            # Base case, stop moment
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            

            memo[key] = solve(m-1, n) + solve(m, n-1)
            return memo[key]

        # Return the answer
        return solve(m, n)


obj = Solution()
print(obj.uniquePaths(3, 7))             # 28
print(obj.uniquePaths(3, 2))             # 3
print(obj.uniquePaths(23, 12))           # 193536720

# T.C: O(M * N)
# S.C: O(M * N)
'''



# Tabulation
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # List Comprehension
        # dp = [ [0] * (n + 1) for _ in range(m + 1) ]

        # DP table, (m,n)th position holds answer
        dp = []
        for _ in range(m + 1):
            dp.append([0] * (n + 1))

        # Set default values
        dp[1][1] = 1

        # Looping till (m,n)
        for i in range(m+1):
            for j in range(n+1):
                current = dp[i][j]

                # Boundary checking
                if i+1 <= m:
                    dp[i+1][j] += current
                    
                # Boundary checking
                if j+1 <= n:
                    dp[i][j+1] += current

        # Return answer
        return dp[m][n]


obj = Solution()
print(obj.uniquePaths(3, 7))             # 28
print(obj.uniquePaths(3, 2))             # 3
print(obj.uniquePaths(23, 12))           # 193536720

# T.C: O(M * N)
# S.C: O(M * N)
'''



# Tabulation (Space optimized)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # DP table, (m,n)th position holds answer
        dp = [1] * (n)

        # Looping till (m,n)
        for _ in range(m - 1):
            for j in range(1, n):
            
                dp[j] = dp[j] + dp[j-1]

        # Return answer
        return dp[n-1]


obj = Solution()
print(obj.uniquePaths(3, 7))             # 28
print(obj.uniquePaths(3, 2))             # 3
print(obj.uniquePaths(23, 12))           # 193536720

# T.C: O(M * N)
# S.C: O(M * N)