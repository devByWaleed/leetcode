class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        st = []
        remove = []     # To keep track of invalid parenthesis

        new_string = ""

        # Loop for valid pairs
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            elif s[i] == ")":
                if st:
                    st.pop()
                elif not st:
                    remove.append(i)
            else:
                continue

        remove += st    # Extend remove to get all invalid indices

        # Making new string
        for i in range(len(s)):
            if i in remove:
                continue
            else:
                new_string += s[i]

        
        return new_string

                    
obj = Solution()
print(obj.minRemoveToMakeValid("lee(t(c)o)de)"))        # lee(t(co)de) / lee(t(c)ode) / lee(t(c)o)de
print(obj.minRemoveToMakeValid("a)b(c)d"))              # ab(c)d
print(obj.minRemoveToMakeValid("))(("))                 # ""

# T.C: O(N)
# S.C: O(N)