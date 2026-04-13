from typing import List

# Recursion
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def solve(i):
            # Base case
            if i >= n:
                return 0

            # For 1 step
            skip = solve(i+1)
                

            # Recursive calculation
            rob = nums[i] + solve(i+2)

            return max(skip, rob)
        
        # Return the answer      
        return solve(0)
    

obj = Solution()
print(obj.rob([1, 2, 3, 1]))            # 4
print(obj.rob([2, 7, 9, 3, 1]))         # 12

# T.C: O(2 ^ N)
# S.C: O(N)
'''



# Memoization
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memo table
        memo = {}

        n = len(nums)

        if n == 1:
            return nums[0]
        
        def solve(i):
            # Lookup in memo for quick result
            if i in memo:
                return memo[i]
            
            # Base case
            if i >= n:
                return 0

            # Skip: Adjacent
            skip = solve(i+1)
                
            # Rob: Current & 2nd previous
            rob = nums[i] + solve(i+2)

            # Max money should be robbed
            memo[i] = max(skip, rob)
            return memo[i]
        
        # Return the answer      
        return solve(0)
    

obj = Solution()
print(obj.rob([1, 2, 3, 1]))            # 4
print(obj.rob([2, 7, 9, 3, 1]))         # 12

# T.C: O(N)
# S.C: O(N)
'''



# Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # DP table, (n)th position holds answer
        dp = [0] * (n)

        if n == 1:
            return nums[0]

        # Set default values
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Looping till n
        for i in range(2, n):
            # Skip: Adjacent
            skip = dp[i-1]
            
            # Rob: Current & 2nd previous
            rob = nums[i] + dp[i-2]
            
            # Max money should be robbed
            dp[i] = max(skip, rob)

        # Return answer
        return dp[n-1]


obj = Solution()
print(obj.rob([1, 2, 3, 1]))            # 4
print(obj.rob([2, 7, 9, 3, 1]))         # 12

# T.C: O(N)
# S.C: O(N)



# 2 Var
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # Set default values
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        # Looping till n
        for i in range(2, n):
            # Calculation
            temp = max(nums[i] + rob1, rob2)

            # Move var1 to next position
            rob1 = rob2
            
            # Move var2 to next position
            rob2 = temp

        # Return answer
        return rob2


obj = Solution()
print(obj.rob([1, 2, 3, 1]))            # 4
print(obj.rob([2, 7, 9, 3, 1]))         # 12

# T.C: O(N)
# S.C: O(1)
'''