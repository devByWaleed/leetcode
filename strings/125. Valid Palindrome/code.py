class Solution:
    def isPalindrome(self, s):
        # New string
        cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        n = len(cleaned_text)

        # 2 Pointers
        left, right = 0, n - 1

        while left < right:
            # Checking for palindrome
            if cleaned_text[left] != cleaned_text[right]:
                return False
            else:
                # Pointer movement
                left += 1
                right -= 1

        # String in palindrome
        return True

        
obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal:Panama"))    # True
print(obj.isPalindrome(" "))                                # True
print(obj.isPalindrome("race a car"))                       # False
print(obj.isPalindrome("0P"))                               # False

# T.C: O(N)     —> Looping through string
# S.C: O(1)     —> No data structure used