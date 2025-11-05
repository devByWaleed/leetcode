class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
                '(':')',
                '{':'}',
                '[':']'
                }
        
        for i in range(len(s)):

            # For opening one
            if s[i] in pairs.keys():
                stack.append(s[i])

            # For closing one 
            elif s[i] in pairs.values():
                if not stack:
                    return False
                
                top_element = stack.pop()
                if s[i] != pairs[top_element]:
                    return False
                
        return True if not stack else False
    
    
obj = Solution()
print(obj.isValid("()"))        # True
print(obj.isValid("()[]{}"))    # True
print(obj.isValid("(]"))        # False
print(obj.isValid("([])"))      # True
print(obj.isValid("([)]"))      # False

# T.C: O(N)
# S.C: O(N)