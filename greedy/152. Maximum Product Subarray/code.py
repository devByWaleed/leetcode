from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = max_product = min_product = nums[0]

        for i in range(1, n):
            # Negative number handling ; max_products always evaluates to higer product
            if nums[i] < 0:
                max_product, min_product = min_product, max_product


            # Minimum of 2 choices
            # Choice 1: Creating new sub-array ; Choice 2: Extending current window
            min_product = min(nums[i], min_product * nums[i])

            # Maximum of 2 choices
            # Choice 1: Creating new sub-array ; Choice 2: Extending current window
            max_product = max(nums[i], max_product * nums[i])

            ans = max(ans, max_product)

        return ans


obj = Solution()
print(obj.maxProduct([2, 3, -2, 4]))             # 6
print(obj.maxProduct([-2, 0, -1]))               # 0
print(obj.maxProduct([-2, 3, -4]))               # 24
print(obj.maxProduct([2, -5, -2, -4, 3]))        # 6

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> No data structure used