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



# Time Limit Exceeded
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