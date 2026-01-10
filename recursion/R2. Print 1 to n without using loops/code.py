class Solution:
    def printTillN(self, N):
        # Base case
        if N == 0:
            return
            
        # Recursive call to go-to base case
        self.printTillN(N-1)
        
        # Printing values in ascending order
        print(N, end=" ")


obj = Solution()
obj.printTillN(5)       # 1 2 3 4 5
obj.printTillN(10)      # 1 2 3 4 5 6 7 8 9 10