class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s1, t1 = "", ""

        # Loop on s
        for i in range(len(s)):

            if s[i] == "#" and s1:
                # Remove last element
                s1 = s1[:len(s1)-1]
            elif s[i] != "#":
                s1 += s[i]
        
        # Loop on t
        for i in range(len(t)):
            if t[i] == "#" and t1:
                # Remove last element
                t1 = t1[:len(t1)-1]
            elif t[i] != "#":
                t1 += t[i]

        # Compare both strings
        return s1 == t1


obj = Solution()
print(obj.backspaceCompare("a", "aa#a"))                   # False
print(obj.backspaceCompare("ab#c", "ad#c"))                # True
print(obj.backspaceCompare("ab##", "c#d#"))                # True
print(obj.backspaceCompare("a#c", "b"))                    # False
print(obj.backspaceCompare("y#fo##f", "y#f#o##f"))         # True

# T.C: O(M + N)
# S.C: O(M + N)