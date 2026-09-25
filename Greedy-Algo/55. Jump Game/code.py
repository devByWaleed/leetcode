class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        # Edge case: 1 jump
        if n == 1:
            return True

        max_reach = 0

        for i, jump in enumerate(nums):
            # Index out of bound
            if i > max_reach:
                return False
            
            # Update max_reach with index after jump
            max_reach = max(max_reach, i + jump)

            # If we comes to last index
            if max_reach >= n - 1:
                return True
        
        # Can't reach
        return False


obj = Solution()
print(obj.canJump([2,3,1,1,4]))     # True
print(obj.canJump([3,2,1,0,4]))     # False

# T.C: O(N)     --> Looping through N numbers
# S.C: O(1)     --> No data structure used
