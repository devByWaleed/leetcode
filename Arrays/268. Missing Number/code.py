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