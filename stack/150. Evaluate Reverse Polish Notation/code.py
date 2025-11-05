from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {"+", "-", "*", "/"}        

        for i in range(len(tokens)):

            # If number , add to stack
            if tokens[i].lstrip("-").isdigit():
                st.append(int(tokens[i]))
            
            # If operator, pop 2 numbers
            elif tokens[i] in operators:
                n2 = st.pop()
                n1 = st.pop()

                # Solving expression
                if tokens[i] == "+":
                    st.append(n1 + n2)
                elif tokens[i] == "-":
                    st.append(n1 - n2)
                elif tokens[i] == "*":
                    st.append(n1 * n2)
                else:
                    st.append(int(n1 / n2))     # Truncate to zero


        return st[0]    # Final value


obj = Solution()
print(obj.evalRPN(["2", "1", "+", "3", "*"]))       # 9
print(obj.evalRPN(["4", "13", "5", "/", "+"]))      # 6
print(obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))   # 22

# T.C: O(N)
# S.C: O(N)