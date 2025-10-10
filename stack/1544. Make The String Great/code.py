class Solution:
    def makeGood(self, s: str) -> str:
        
        # Edge case
        if len(s) == 0 or len(s) == 1:
            return s
        
        st = []
        new_string = ""

        # Handling stack with string
        for i in range(len(s)):
            if not st:
                st.append(s[i])
            else:
                # If adjacent pair, remove from stack
                if s[i].lower() == st[-1].lower() and s[i] != st[-1]:
                    st.pop()
                # Else add current to stack
                else:
                    st.append(s[i])
        
        # Creating new string
        while st:
            new_string += st[-1]
            st.pop()

        # Reversing the string
        new_string = reversed(new_string)
        return "".join(new_string)


obj = Solution()
print(obj.makeGood("leEeetcode"))       # leetcode
print(obj.makeGood("abBAcC"))           # ""
print(obj.makeGood("s"))                # s

# T.C: O(N)
# S.C: O(N)