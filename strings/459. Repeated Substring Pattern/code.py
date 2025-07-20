class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # Doubling the original string
        double = s + s

        # Remove 1st and last character
        double = double[1: len(double)-1]

        # find() method to check index. If -1, it is not a sub-string pattern
        value = double.find(s) 
        return value != -1


obj = Solution()
print(obj.repeatedSubstringPattern("abab"))             # True
print(obj.repeatedSubstringPattern("aba"))              # False
print(obj.repeatedSubstringPattern("abcabcabcabc"))     # True

# T.C: O(N)
# S.C: O(N)