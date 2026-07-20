class Solution:
    def reverse(self, x: int) -> int:
        # Test case: single number
        if -9 <= x <= 9:
            return x
        
        # For handling -ve numbers
        sign = 0
        # Copy for the input remained unchanged
        num = x
        # Final reversed integer
        result = 0

        if num < 0:
            sign = -1
            # Converting to positive
            num = num * sign
        
        # Loop condition
        while num != 0:
            # Get last digit
            last_digit  = num % 10

            # Add to result
            result = (result * 10) + last_digit

            # Discard last extracted digit
            num = num // 10

        # If number was -ve, convert it back to -ve
        if sign == -1:
            result = result * sign

        # Integer range check
        if result > 2**31 - 1 or result < -2**31:
            return 0 
        
        return result


obj = Solution()
print(obj.reverse(123))     # 321
print(obj.reverse(-123))     # -321
print(obj.reverse(120))     # 21
print(obj.reverse(-2147483648))     # 21

# T.C: O(LOG |x|)
# S.C: O(1)