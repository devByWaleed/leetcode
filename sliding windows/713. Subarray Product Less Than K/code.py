from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0       # Count sub-arrays

        product = 1     # running product

        left = 0        # To shrink window

        for right in range(len(nums)):

            # Muliply current value
            product *= nums[right]

            # If product is not valid, shrink window
            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            
            # Adding all sub-arrays from left to right
            count += right - left + 1

        return count


obj = Solution()
print(obj.numSubarrayProductLessThanK([10, 5, 2, 6], 100))     # 8
print(obj.numSubarrayProductLessThanK([1, 2, 3], 0))           # 0

# T.C: O(N)
# S.C: O(1)



# Time Limit Exceeded (Brute Force)
'''
from typing import List
from functools import reduce

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0

        for right in range(len(nums)):

            left = right    # Setting left pointer

            # condition for expanding window
            while left != len(nums):
                
                product_lambda = lambda x, y: x * y
                
                array_product = reduce(product_lambda, nums[right: left+1])
                
                # Condition for counting sub-arrays
                if array_product < k:
                    count += 1
                
                left += 1       # Expanding window


        return count


obj = Solution()
print(obj.numSubarrayProductLessThanK([10, 5, 2, 6], 100))     # 8
print(obj.numSubarrayProductLessThanK([1, 2, 3], 0))           # 0

T.C: O(N ^ 3)
S.C: O(N)
'''