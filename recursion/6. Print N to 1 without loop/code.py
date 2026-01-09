class Solution:
    def printNos(self, n):
        # Base case
        if n == 0:
            return
        
        # Printing values
        print(n, end=" ")
        
        # Recursive call
        self.printNos(n-1)


obj = Solution()
obj.printNos(10)     # 10 9 8 7 6 5 4 3 2 1