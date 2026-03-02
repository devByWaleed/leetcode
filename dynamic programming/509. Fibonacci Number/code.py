class Solution:
    def fib(self, n: int) -> int:
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
print(obj.fib(2))       # 1
print(obj.fib(3))       # 2
print(obj.fib(4))       # 3

# T.C: O(N)
# S.C: O(N)