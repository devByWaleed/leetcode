class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Base cases
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        
        if x // 10 == 0:
            return True     # For single digit number
        

        # Helper function to reverse the number
        def reverse(x, reversed_num = 0):
            # Base case to stop
            if x == 0:
                return reversed_num

            last_digit = x % 10
            remaining = x // 10

            # Recursive call for remaining number
            return reverse(remaining, (reversed_num * 10) + last_digit)
        

        # Compare original and reversed one
        return x == reverse(x)


obj = Solution()
print(obj.isPalindrome(121))       # True
print(obj.isPalindrome(123))       # False
print(obj.isPalindrome(0))         # True
print(obj.isPalindrome(7))         # True

# T.C: O(LOG(N))
# S.C: O(LOG(N))