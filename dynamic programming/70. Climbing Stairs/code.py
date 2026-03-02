class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case
        if n <= 2:
            return n
        
        # Initialize dp table
        dp = [0] * (n + 1)

        # Initialize initial cases
        dp[1] = 1
        dp[2] = 2

        # Looping & storing previous number
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        # Return answer for nth number (given)
        return dp[n]


obj = Solution()
print(obj.climbStairs(2))       # 2
print(obj.climbStairs(3))       # 3


# T.C: O(N)
# S.C: O(N)







'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # Size n+1 to include "0 -> n"
        memo = [-1] * (n + 1)
        
        def solve(memo, n):
            # Base case
            if n <= 1:
                return n
    
            # If already have final answer, return
            if memo[n] != -1:
                return memo[n]
            
            # Calculating fibonacci number
            memo[n] = solve(memo, n-1) + solve(memo, n-2)

            # Returning answer
            return memo[n]

        # Final return
        return solve(memo, n)


obj = Solution()
print(obj.climbStairs(2))       # 2
print(obj.climbStairs(3))       # 3
'''