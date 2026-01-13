class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base cases
        if n == 1:  return x
        if n == 0:  return 1
        '''
        if n == 0 or x == 0:  return 1   # x > 0 (guaranteed)
        '''

        # If n is negative
        if n < 0:
            # To make n +ve
            n = abs(n)

            # Calculation
            result = self.myPow(x, n)

            # Invert the result
            return 1 / result

        else:
            # Pre-calculate to reduce operations
            half = self.myPow(x, n // 2)

            # If n is even
            if n % 2 == 0:
                return half * half
            
            # If n is odd, remove one x
            else:
                return half * half * x


obj = Solution()
print(obj.myPow(2.00000, 10))       # 1024.00000
print(obj.myPow(2.10000, 3))        # 9.26100
print(obj.myPow(2.00000, -2))       # 0.25000

# T.C: O(LOG(N))
# S.C: O(LOG(N))