# Tabulation
class Solution:
    def fib(self, n: int) -> int:
        # DP table, (n+1)th position holds answer
        dp = [0] * (n + 1)
        
        # Set default values
        dp[1] = 1
        
        # Looping till n
        for i in range(2, n+1):
            # Running sum calculation
            dp[i] = dp[i-1] + dp[i-2]

        # Return answer
        return dp[n]


obj = Solution()
print(obj.fib(2))       # 1
print(obj.fib(3))       # 2
print(obj.fib(4))       # 3

# T.C: O(N)
# S.C: O(N)



# Memoization
'''
class Solution:
    def fib(self, n: int) -> int:
        # Memo table
        memo = {}
        
        def solve(k):
            # Lookup in memo for quick result
            if k in memo:
                return memo[k]
            
            # Base case
            if k <= 1:
                return k
            
            # Last 2 numbers
            num1 = solve(k-1)
            num2 = solve(k-2)
            
            # Recursive calculation
            memo[k] = num1 + num2

            return memo[k]
        
        # Return the answer
        return solve(n)
        
        
obj = Solution()
print(obj.fib(2))       # 1
print(obj.fib(3))       # 2
print(obj.fib(4))       # 3

# T.C: O(N)
# S.C: O(N)
'''



# Recursion
'''
class Solution:
    def fib(self, n: int) -> int:
        # Base case
        if n == 0 or n == 1:
            return n
        
        # Last 2 numbers
        num1 = self.fib(n-1)
        num2 = self.fib(n-2)

        # Recursive calculation
        return num1 + num2


obj = Solution()
print(obj.fib(2))       # 1
print(obj.fib(3))       # 2
print(obj.fib(4))       # 3

# T.C: O(2 ^ N)
# S.C: O(N)
'''



# 2 Var
'''
class Solution:
    def fib(self, n: int) -> int:
        # Edge cases
        if n == 0 or n == 1:
            return n
        
        # 2 vars
        var1 = 0
        var2 = 1

        # Looping till n
        for _ in range(2, n+1):
            # F(i) = F(i-1) + F(i-2)
            temp = var1 + var2
            
            # Move var1 to next position
            var1 = var2
            
            # Move var2 to next position
            var2 = temp

        # Return answer
        return var2


obj = Solution()
print(obj.fib(2))       # 1
print(obj.fib(3))       # 2
print(obj.fib(4))       # 3

# T.C: O(N)
# S.C: O(1)
'''