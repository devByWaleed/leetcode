from typing import List

'''
Pattern: Accumulation / Running Product

- prefix (1st pass) => answer[i] is product of all elements to left of "nums" array
- suffix (2nd pass) => answer[i] is product of all elements to right+left (final answer) of "nums" array
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Static array of n length
        answer = [1] * n

        # First Part, finding prefixes
        prefix_product = 1

        # Forward looping to find prefix product
        for i in range(n):
            answer[i] = answer[i] * prefix_product
            
            # update the values with the product
            prefix_product = prefix_product * nums[i]


        # Second Part, finding suffixes
        suffix_product = 1

        # Reverse looping to find suffix product
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * suffix_product
        
            # update the values with the product
            suffix_product = suffix_product * nums[i]


        return answer


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))          # [24, 12, 8, 6]
print(obj.productExceptSelf([-1, 1, 0, -3, 3]))     # [0, 0, 9, 0, 0]

# T.C: O(N)
# S.C: O(N)