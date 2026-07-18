class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask of 32-bit to handle Python's integer
        mask = 0xFFFFFFFF
        
        # Save copy
        num1, num2 = a & mask, b & mask
        
        #while num2 != 0:
        while num1 != 0:
            # Save carry for bigger numbers
            carry = (num1 & num2) & mask
            
            # XOR done sum without carry
            #num1 = (num1 ^ num2) & mask
            num2 = (num1 ^ num2) & mask
            
            # Shift carry by 1 and store it for later sum
            #num2 = (carry << 1) & mask
            num1 = (carry << 1) & mask
         
        # If number is -ve, convert num2 back to -ve
        if num2 > 0x7FFFFFFF:
            return ~(num2 ^ mask)
            
        return num2
        #return num1


obj = Solution()
print(obj.getSum(1, 2))     # 3
print(obj.getSum(2, 3))     # 5

# T.C: O(1)
# S.C: O(1)