from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        # Edge case
        if n == 1:    return int(tokens[0])

        stack = []

        # For constant lookup
        operators = {"+", "-", "*", "/"}
        
        for i in range(n):
            curr = tokens[i]

            # Pushing number to stack
            if curr not in operators:
                stack.append(curr)
            else:
                # Order matters
                num2 = stack.pop()
                num1 = stack.pop()

                res = eval(f"{num1}{curr}{num2}")

                # Truncated to 0
                res = int(res)

                # Pushing result to stack
                stack.append(res)

        # Top element is answer
        return stack[-1]


obj = Solution()
print(obj.evalRPN(["2", "1", "+", "3", "*"]))       # 9
print(obj.evalRPN(["4", "13", "5", "/", "+"]))      # 6
print(obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))   # 22
print(obj.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))       # -7

# T.C: O(N)
# S.C: O(N)