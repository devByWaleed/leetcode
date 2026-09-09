class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for verifying pair
        stack = []

        for i in range(len(s)):
            # For opening
            if s[i] == "(" or s[i] ==  "{" or s[i] ==  "[":
                stack.append(s[i])
            else:
                if stack:
                    top = stack.pop()
                    
                    # Pair Matching
                    if (
                        (top == "(" and s[i] == ")") or 
                        (top == "{" and s[i] == "}") or 
                        (top == "[" and s[i] == "]")
                    ):
                        continue
                    else:
                        # No matching pair
                        return False
                # Stack is empty
                else:
                    return False


        # If stack is empty, parenthesis is valid
        return False if stack else True

        
obj = Solution()
print(obj.isValid("()"))        # True
print(obj.isValid("()[]{}"))    # True
print(obj.isValid("(]"))        # False
print(obj.isValid("([])"))      # True
print(obj.isValid("([)]"))      # False

# T.C: O(N)     —> Looping through string
# S.C: O(1)     —> Stack data structure used