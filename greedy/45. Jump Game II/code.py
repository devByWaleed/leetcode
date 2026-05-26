from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge case
        if n == 1:
            return 0
        
        # Total jumps
        jumps = 0

        # Index you can reach
        current_end = 0

        # Index you can reach overall by jumping from any index
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                # Increase jumps
                jumps += 1

                # Update by new end for jumps
                current_end = farthest

        return jumps


obj = Solution()
print(obj.jump([2, 3, 1, 1, 4]))      # 2
print(obj.jump([2, 3, 0, 1, 4]))      # 2

# T.C: O(N)
# S.C: O(1)