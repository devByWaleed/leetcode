from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Static array of n length
        answer = [1] * n

        # Prefix: all elements to left
        prefix_product = 1

        # Suffix: all elements to right
        suffix_product = 1

        for i in range(n):
            # Update answer[i] with respective product
            answer[i] = answer[i] * prefix_product
            
            # Update the prefix product current index value
            prefix_product = prefix_product * nums[i]

            # Update answer[n-1-i] with respective product
            answer[n-1-i] = answer[n-1-i] * suffix_product
        
            # Update the suffix product current index value
            suffix_product = suffix_product * nums[n-1-i]

        return answer


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))          # [24, 12, 8, 6]
print(obj.productExceptSelf([-1, 1, 0, -3, 3]))     # [0, 0, 9, 0, 0]

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> As per description

# Follow up: Can you solve the problem in O(1) extra space complexity? 
# (The output array does not count as extra space for space complexity analysis.)
# ANSWER: Yes. As output array doesn't count as extra space this algorithm solves the problem in O(1) extra space complexity


# 2 PASS
'''
from typing import List

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

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> As per description

# Follow up: Can you solve the problem in O(1) extra space complexity? 
# (The output array does not count as extra space for space complexity analysis.)
# ANSWER: Yes. As output array doesn't count as extra space this algorithm solves the problem in O(1) extra space complexity
'''