class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        n = len(s)

        st = []

        new_string = ""

        # Manage stack
        for i in range(n):
            if not st or s[i] != st[-1]:
                st.append(s[i])
            elif s[i] == st[-1]:
                st.pop()

        # Add elements to new string
        while st:
            new_string += st[-1]
            st.pop()

        # Reversing new string
        new_string = reversed(new_string)
        return "".join(list(new_string))


obj = Solution()
print(obj.removeDuplicates("abbaca"))   # ca
print(obj.removeDuplicates("azxxzy"))   # ay

# T.C: O(N)
# S.C: O(N)


# Brute Force
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        n = len(s)

        new_string = ""

        for i in range(n):
            if not new_string or s[i] != new_string[-1]:
                new_string += s[i]
            else:
                new_string = new_string[:-1]
        
        return new_string

obj = Solution()
print(obj.removeDuplicates("abbaca"))   # ca
print(obj.removeDuplicates("azxxzy"))   # ay

# T.C: O(N ^ 2)
# S.C: O(N)
'''