class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)

        # Edge case
        if n == 1:
            return True
        

        def isPalindrome(s, left, right):

            while left <= right:
            
                # Return False as per palindrome condition
                if s[left] != s[right]:
                    return False
                
                # Moving the pointers
                left += 1
                right -= 1
        
            return True     # After looping, return True for a palindrome



        # 2 Pointers pointing at start and end of string
        left = 0
        right = n - 1

        # Condition forr looping over the string of even & odd length
        while left <= right:
            
            # As per condition of removing at most 1 char, we declare helping function for checking
            if s[left] != s[right]:

                # We have 2 conditions, either the different char is on left side or right side
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
        
            # Moving the pointers
            left += 1
            right -= 1

        return True  # After looping, return True for a palindrome


obj = Solution()
print(obj.validPalindrome("abca"))      # True
print(obj.validPalindrome("aba"))       # True
print(obj.validPalindrome("abc"))       # False

# T.C: O(N)
# S.C: O(1)