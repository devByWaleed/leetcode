class Solution:
    def factorial(self, n: int) -> int:
        # Base case
        if n == 0 or n == 1:
            return 1
        
        # Recursive calls + factorial calculation
        return n * self.factorial(n-1)


obj = Solution()
print(obj.factorial(4))       # 24
print(obj.factorial(0))       # 1
print(obj.factorial(1))       # 1
print(obj.factorial(20))      # 2.432902e+18 / 2432902008176640000

# T.C: O(N)
# S.C: O(N)