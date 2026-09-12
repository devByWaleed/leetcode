class Solution:
    def isPalindrome(self, s):
        # New string
        # cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        # n = len(cleaned_text)

        n = len(s)
        # 2 Pointers
        left, right = 0, n - 1

        while left < right:
            # If left pointer encounter non-alphanumeric chars
            if not s[left].isalnum() or s[left] == " ":
                left += 1
                continue

            # If right pointer encounter non-alphanumeric chars
            if not s[right].isalnum() or s[right] == " ":
                right -= 1
                continue
            # Checking for palindrome
            if s[left].lower() != s[right].lower():
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