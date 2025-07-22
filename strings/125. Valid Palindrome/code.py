import re

class Solution:

    def isPalindrome(self, s):
        
        s = s.replace(" ", "")

        s = s.lower()

        s = re.sub(r'[^a-zA-Z0-9]', "", s)

        if s == "":     return True

        n = len(s)

        l = 0
        r = n - 1

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True


obj = Solution()

print(obj.isPalindrome("race a car"))
print(obj.isPalindrome(" "))
print(obj.isPalindrome("A man, a plan, a canal:Panama"))
print(obj.isPalindrome("0P"))

# T.C: O(N)
# S.C: O(1)