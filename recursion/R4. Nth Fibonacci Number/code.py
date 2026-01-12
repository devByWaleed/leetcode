class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Base case
        if n == 0 or n == 1:
            return n
        
        # Recursive calls + summation of prev 2 numbers
        return self.nthFibonacci(n-1) + self.nthFibonacci(n-2)


obj = Solution()
print(obj.nthFibonacci(5))       # 5
print(obj.nthFibonacci(0))       # 0
print(obj.nthFibonacci(1))       # 1
print(obj.nthFibonacci(30))      # 832040

# T.C: O(2 ^ N)
# S.C: O(N)