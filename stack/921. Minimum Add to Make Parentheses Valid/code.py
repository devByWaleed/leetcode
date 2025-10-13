class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        count = 0       # For pairs if stack is empty
        
        for i in range(len(s)):

            # For opening one
            if s[i] == "(":
                stack.append(s[i])

            # For closing one 
            elif s[i] == ")":

                # If stack is not empty, then check for valid pair
                if stack:
                    top_element = stack.pop()
                    if top_element == "(":
                        continue

                # If stack is empty, increment counter
                else:
                    count += 1
                
        # Returning length + count as it handles both condition
        return len(stack) + count
    

obj = Solution()
print(obj.minAddToMakeValid("())"))     # 1
print(obj.minAddToMakeValid("((("))     # 3
print(obj.minAddToMakeValid("(()("))    # 2
print(obj.minAddToMakeValid("((())"))   # 1

# T.C: O(N)
# S.C: O(N)


# Not Correct
'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        st = []

        count = 0

        for i in range(len(s)):
            if s[i] == "(":
                if "(" in st:
                    count += 1
                    continue
                st.append(s[i])
            
            elif s[i] == ")":
                if not st:
                    count += 1
                if st:
                    top_element = st.pop()
                    if top_element == "(":
                        continue

        
        if s[len(s)-1] == "(":  count += 1

        return count


obj = Solution()
print(obj.minAddToMakeValid("((())"))   # 1, but 3 given
print(obj.minAddToMakeValid("())"))     # 1
print(obj.minAddToMakeValid("((("))     # 3
print(obj.minAddToMakeValid("(()("))    # 2
'''