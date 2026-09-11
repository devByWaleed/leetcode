class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pointer1, pointer2 = 0, 0

        # Pointer1 for iteration on t
        while pointer1 < len(t):

            # If values are equal and in range of length, increase pointer2
            if pointer2 < len(s) and s[pointer2] == t[pointer1]:
                pointer2 += 1
            
            pointer1 += 1

        # Compairing the numbers
        return pointer2 == len(s)


obj = Solution()
print(obj.isSubsequence("abc", "ahbgdc"))       # True
print(obj.isSubsequence("axc", "ahbgdc"))       # False

# T.C: O(len(t))
# S.C: O(1)