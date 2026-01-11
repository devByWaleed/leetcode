class Solution:
    def sumOfNaturals(self, n):
        # Base case
        if n == 0:
            return 0
        
        # Recursive calls + summation
        return n + self.sumOfNaturals(n-1)


obj = Solution()
print(obj.sumOfNaturals(6))     # 21
print(obj.sumOfNaturals(4))     # 10
print(obj.sumOfNaturals(0))     # 0

# T.C: O(N)
# S.C: O(N)