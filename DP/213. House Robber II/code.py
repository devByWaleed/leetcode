from typing import List

# Recursion
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def solve(houses, i):
            n = len(houses)

            # Base case
            if i >= n:
                return 0

            # Skip: Adjacent
            skip = solve(houses, i+1)
                
            # Rob: Current & 2nd previous
            rob = nums[i] + solve(houses, i+2)

            return max(skip, rob)
        

        # Return the answer      
        return max(
            # Exclude 1st house
            solve(nums[1:], 0),
            
            # Exclude last house 
            solve(nums[:-1], 0)
        )
    
    
obj = Solution()
print(obj.rob([2, 3, 2]))            # 3
print(obj.rob([1, 2, 3, 1]))         # 4
print(obj.rob([1, 2, 3]))            # 3

# T.C: O(2 ^ N)
# S.C: O(N)
'''



# Memoization
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        def solve(houses, i, memo):
            # Lookup in memo for quick result
            if i in memo:
                return memo[i]

            # Base case
            if i >= len(houses):
                return 0

            # Skip: Adjacent
            skip = solve(houses, i+1, memo)
                
            # Rob: Current & 2nd previous
            rob = houses[i] + solve(houses, i+2, memo)

            # Max money should be robbed
            memo[i] = max(skip, rob)
            return memo[i]
        

        # Return the answer      
        return max(
            # Exclude 1st house
            solve(nums[1:], 0, {}),
            
            # Exclude last house 
            solve(nums[:-1], 0, {})
        )
    
    
obj = Solution()
print(obj.rob([2, 3, 2]))            # 3
print(obj.rob([1, 2, 3, 1]))         # 4
print(obj.rob([1, 2, 3]))            # 3

# T.C: O(N)
# S.C: O(N)
'''



# Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: Single house
        if n == 1:
            return nums[0]

        def rob_helper(nums, start, end):
            length = end - start

            # If the slice is empty (happens with very small inputs)
            if length == 0: return 0
            # If the slice has one house, max is just that house
            if length == 1: return nums[start]

            # DP array
            dp = [0] * length

            # Set default robbed values
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start+1])

            for i in range(2, length):
                # SKIP
                skip = dp[i-1]

                # ROB: Ignore adjacent house
                # Mapped i to nums index
                rob = nums[start+i] + dp[i-2]

                # Save maximum amount
                dp[i] = max(skip, rob)

            # Last index holds answer
            return dp[length-1]

        # SKIP last house
        con1 = rob_helper(nums, 0, n-1)

        # SKIP 1st house
        con2 = rob_helper(nums, 1, n)

        # MAX from circular condition
        return max(con1, con2)


obj = Solution()
print(obj.rob([2, 3, 2]))            # 3
print(obj.rob([1, 2, 3, 1]))         # 4
print(obj.rob([1, 2, 3]))            # 3
print(obj.rob([1, 2, 1, 1]))            # 3

# T.C: O(N)     --> Running loop on N numbers
# S.C: O(N)     --> DP array of N size used



# 2 Var
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        def solve(houses):
            n_sub = len(houses)
            
            # Manual handle for short slices to prevent IndexErrors
            if n_sub == 0: return 0
            if n_sub == 1: return houses[0]

            # Set default values
            rob1 = houses[0]
            rob2 = max(houses[0], houses[1])

            # Looping till n
            for i in range(2, n_sub):
                # Calculation
                temp = max(houses[i] + rob1, rob2)

                # Move var1 to next position
                rob1 = rob2
                
                # Move var2 to next position
                rob2 = temp

            # Return answer
            return rob2
    
        # Return the answer      
        return max(
            # Exclude 1st house
            solve(nums[1:]),
            
            # Exclude last house 
            solve(nums[:-1])
        )
    

obj = Solution()
print(obj.rob([2, 3, 2]))            # 3
print(obj.rob([1, 2, 3, 1]))         # 4
print(obj.rob([1, 2, 3]))            # 3

# T.C: O(N)
# S.C: O(1)
'''