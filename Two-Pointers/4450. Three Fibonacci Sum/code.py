class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        l, r = 0, 1
        sum_3 = l + r

        while (sum_3 + r + l) <= n:
            if (sum_3 + r + l) == n:
                return True
            else: 
                l = r
                r = sum_3
                sum_3 = l + r
        
        return False
        

obj = Solution()
print(obj.threeFibonacciSum(16))
print(obj.threeFibonacciSum(8))
print(obj.threeFibonacciSum(2))

# T.C:  O(N)    --> Loop through ~ N times
# S.C:  O(1)    --> No data structure used
