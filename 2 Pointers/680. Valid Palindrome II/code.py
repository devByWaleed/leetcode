class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)

        # Edge case
        if n == 1:
            return True
            
        # 2 pointers
        l = 0
        r = n - 1
        
        # Helper function to check for deletion
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        
        while l < r:
            if s[l] != s[r]:
                # Deletion from both side 
                return is_palindrome(l+1, r) or is_palindrome(l, r-1)
            
            # Moving both pointers
            else:
                l += 1
                r -= 1
                
        return True


obj = Solution()
print(obj.validPalindrome("abca"))      # True
print(obj.validPalindrome("aba"))       # True
print(obj.validPalindrome("abc"))       # False

# T.C: O(N)
# S.C: O(1)