# XOR operator
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_array = 0
        xor_range = 0

        # XORing array elements
        for number in nums:
            xor_array = xor_array ^ number

        # XORing numbers in given range
        for i in range(0, n+1):
            xor_range = xor_range ^ i

        # Xoring the number itself cancels out, res will be missing number
        res = xor_array ^ xor_range
        return res
    

obj = Solution()

print(obj.missingNumber([3, 0, 1]))                     # 2
print(obj.missingNumber([0, 1]))                        # 2
print(obj.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))   # 8

# T.C = O(N)
# S.C = O(1)




# Using Math
'''
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Math Formula
        total_sum = (n * (n+1)) // 2

        # Sum of array's element
        list_sum = sum(nums)

        # Returns the missing number
        return total_sum - list_sum


obj = Solution()

print(obj.missingNumber([3, 0, 1]))                     # 2
print(obj.missingNumber([0, 1]))                        # 2
print(obj.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))   # 8

# T.C = O(N)
# S.C = O(1)
'''