from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        X = 0
        
        for i in range(0, len(operations)):
          
              # Condition for increment
              if operations[i] == 'X++' or operations[i] == '++X':
                X = X + 1
             
              #  Else decrement 
              else:
                X = X - 1
        
        return X

obj = Solution()
print(obj.finalValueAfterOperations(["--X","X++","X++"]))           # 1
print(obj.finalValueAfterOperations(["++X","++X","X++"]))           # 3
print(obj.finalValueAfterOperations(["X++","++X","--X","X--"]))     # 0

# T.C = O(N)
# S.C = O(1)