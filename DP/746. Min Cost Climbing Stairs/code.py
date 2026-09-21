from typing import List

# Recursion
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def solve(i):
            # Base case
            if i >= n:
                return 0

            # For 1 step
            way1 = solve(i+1)
                
            # For 2 steps
            way2 = solve(i+2)

            # Recursive calculation
            return cost[i] + min(way1, way2)
        
        # Return the answer
        step1 = solve(0)
        step2 = solve(1)
        
        return min(step1, step2)


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))                                  # 15
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))          # 6
'''



# Memoization
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # Memo table
        memo = {}
        
        def solve(i):
            # Lookup in memo for quick result
            if i in memo:
                return memo[i]
            
            # Base case
            if i >= n:
                return 0

            # For 1 step
            way1 = solve(i+1)
                
            # For 2 steps
            way2 = solve(i+2)

            # Recursive calculation
            memo[i] = cost[i] + min(way1, way2)
            
            return memo[i]
        
        # Return the answer
        step1 = solve(0)
        step2 = solve(1)
        
        return min(step1, step2)


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))                                  # 15
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))          # 6

# T.C: O(N)
# S.C: O(N)
'''


# Tabulation
'''
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # DP table, (n+1)th position holds answer
        dp = [0] * (n + 1)

        # Looping till n
        for i in range(2, n+1):
            # For 1 step
            step1 = dp[i-1] + cost[i-1]
            
            # For 2 steps
            step2 = dp[i-2] + cost[i-2]
            
            # Minimum of previous 2 "total costs"
            dp[i] = min(step1, step2)

        # Return answer
        return dp[n]


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))                                  # 15
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))          # 6

# T.C: O(N)
# S.C: O(N)
# ------------------- or
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # DP table, (n+2)th position for boundary
        dp = [0] * (n + 2)

        # Looping till 0
        for i in range(n-1, -1, -1):
            
            # Minimum of previous 2 "total costs"
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        # Return answer
        return min(dp[0], dp[1])


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))                                  # 15
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))          # 6

# T.C: O(N)
# S.C: O(N)
'''



# 2 Var
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # 2 vars
        two_step = 0
        one_step = 0

        # Looping till n
        for i in range(n-1, -1, -1):
            # Calculation
            temp = cost[i] + min(two_step, one_step)
            
            # Move var1 to next position
            two_step = one_step
            
            # Move var2 to next position
            one_step = temp

        # Return answer
        return min(two_step, one_step)


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))                                  # 15
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))          # 6

# T.C: O(N)
# S.C: O(1)
'''