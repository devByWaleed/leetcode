from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Edge case
        if n == 1:
          return ["()"]
          
        # For pairs and final answer
        ans, pair = [], []
          
        # Helper function to create pair
        def backtrack(open, close):
          
          # Adding final pair to answer
          if len(pair) == 2*n:
            ans.append("".join(pair))
            return
          
          # Opening must be in limit
          if open < n:
            pair.append("(")
            backtrack(open+1, close)
            pair.pop()
          
          # Move to closing after limit exceeded
          if open > close:
            pair.append(")")
            backtrack(open, close+1)
            pair.pop()
          
        
        # Calling function with 0 as 
        backtrack(0, 0)
        
        return ans


obj = Solution()
print(obj.generateParenthesis(3))       # ["((()))", "(()())", "(())()", "()(())", "()()()"]
print(obj.generateParenthesis(1))       # ["()"]

# T.C: O(4^N / Sqrt(N))
# S.C: O(N)