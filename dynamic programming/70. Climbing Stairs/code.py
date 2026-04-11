# Tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP table, (n+1)th position holds answer
        dp = [0] * (n + 1)
        
        # Set default values
        dp[1] = 1
        dp[2] = 2
        
        # Looping till n
        for i in range(3, n+1):
            # Running sum calculation
            dp[i] = dp[i-1] + dp[i-2]

        # Return answer
        return dp[n]


obj = Solution()
print(obj.climbStairs(2))       # 2
print(obj.climbStairs(3))       # 3

# T.C: O(N)
# S.C: O(N)



# Memoization
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # Memo table
        memo = {}
        
        def solve(k):
            # Lookup in memo for quick result
            if k in memo:
                return memo[k]
            
            # Base case
            if k <= 2:
                return k
            
            # For 1 step
            way1 = solve(k-1)
            
            # For 2 steps
            way2 = solve(k-2)
            
            # Recursive calculation
            memo[k] = way1 + way2

            return memo[k]
        
        # Return the answer
        return solve(n)


obj = Solution()
print(obj.climbStairs(2))       # 2
print(obj.climbStairs(3))       # 3

# T.C: O(N)
# S.C: O(N)
'''



# Recursion
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case
        if n <= 2:
            return n
        
        # For 1 step
        way1 = self.climbStairs(n-1)
        
        # For 2 steps
        way2 = self.climbStairs(n-2)
        
        # Recursive calculation
        return way1 + way2


obj = Solution()
print(obj.climbStairs(2))       # 2
print(obj.climbStairs(3))       # 3

# T.C: O(2 ^ N)
# S.C: O(N)
'''



# 2 Vars
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # Edge case
        if n <= 2:
            return n
        
        # 2 vars
        var1 = 1
        var2 = 2

        # Looping till n
        for _ in range(3, n+1):
            # cS(i) = cS(i-1) + cS(i-2)
            temp = var1 + var2
            
            # Move var1 to next position
            var1 = var2
            
            # Move var2 to next position
            var2 = temp

        # Return answer
        return var2


obj = Solution()
print(obj.climbStairs(2))       # 2
print(obj.climbStairs(3))       # 3

# T.C: O(N)
# S.C: O(1)
'''