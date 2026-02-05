class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # For constant lookup
        pairs = { "(": ")", "{": "}", "[": "]" }

        for char in s:
            
            # If opening one, push to stack
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:

                # Edge case => empty stack
                if stack:

                    # Popping & matching
                    curr = stack.pop()
                    if pairs[curr] == char:
                        continue
                    # If pair not matches
                    else:
                        return False
                # If stack is empty => invalid pair
                else:
                    return False
            
        # After loop, if stack is empty => True / not empty => False
        return not stack


obj = Solution()
print(obj.isValid("()"))        # True
print(obj.isValid("()[]{}"))    # True
print(obj.isValid("(]"))        # False
print(obj.isValid("([])"))      # True
print(obj.isValid("([)]"))      # False

# T.C: O(N)
# S.C: O(N)