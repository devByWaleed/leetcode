from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        sum_left = [0] * n
        sum_right = [0] * n

        # Leftmost sum for index i
        for i in range(1, n):
            sum_left[i] = sum_left[i-1] + nums[i-1]

        # Rightmost sum for index i
        for j in range(n-2, -1, -1):
            sum_right[j] = sum_right[j+1] + nums[j+1]

        for k in range(n):
            # Find same sum, find pivot index
            if sum_left[k] == sum_right[k]:
                return k

        # No pivot index found
        return -1
    

obj = Solution()
print(obj.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(obj.pivotIndex([1, 2, 3]))           # Output: -1
print(obj.pivotIndex([2, 1, -1]))          # Output: 0

# T.C: O(N)     --> Loop on N times
# S.C: O(N)     --> N size arrays used