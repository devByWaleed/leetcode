class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Edge case
        if len(s) == 1:
            return True
        
        return True


obj = Solution()
print(obj.validPalindrome("aba"))       # True
print(obj.validPalindrome("abca"))      # True
print(obj.validPalindrome("abc"))       # False