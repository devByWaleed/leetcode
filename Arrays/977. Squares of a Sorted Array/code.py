from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(0, len(nums)):

            # Replacing numbers with its squares
            nums[i] = nums[i] * nums[i]

        # Sorting
        nums.sort()

        return nums

obj = Solution()
print(obj.sortedSquares([-4, -1, 0, 3, 10]))        # [0, 1, 9, 16, 100]
print(obj.sortedSquares([-7, -3, 2, 3, 11]))        # [4, 9, 9, 49, 121]

# T.C: O(N log N)
# S.C: O(1)