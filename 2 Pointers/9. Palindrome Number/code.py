class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        # Base case for 1 element ( Palindrome by-default )
        if len(x) == 1:
            return True
        
        n = len(x)
        
        # 2 pointers focusing on 1st and last element
        l = 0
        r = n - 1
        
        # While loop for iterating ( works for both even and odd length )
        while l < r:

            # condition if both elements not matched
            if x[l] != x[r]:
                return False
            
            # Moving the pointers for all elements
            l += 1
            r -= 1

        # After checking whole number, return True 
        return True
    
obj = Solution()
print(obj.isPalindrome(121))    # True
print(obj.isPalindrome(-121))   # False
print(obj.isPalindrome(10))     # False

# T.C: O(D)     D = no. of numbers in x
# S.C: O(D)