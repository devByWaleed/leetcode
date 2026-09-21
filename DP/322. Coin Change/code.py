from typing import List

# Recursion
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
          
        def solve(amount, i):
            # Base case: no amount can be made
            if amount == 0:
                return 0
            
            # Base case: no coins left or amount went negative
            if i >= n or amount < 0:
                return float("inf")

            # TAKE: current coin (stay at same index)
            take = float("inf")
            if amount - coins[i] >= 0:
                take = 1 + solve(amount - coins[i], i)

            # SKIP: move coin to next step
            skip = solve(amount, i + 1)

            # Return the minimum of both options
            return min(take, skip)

        # If get lower coins, return it. Else return -1
        min_coins = solve(amount, 0)
        return -1 if min_coins == float("inf") else min_coins


obj = Solution()
print(obj.coinChange([1, 2, 5], 11))            # 3
print(obj.coinChange([2], 3))                   # -1
print(obj.coinChange([1], 0))                   # 0

# T.C: O(N)
# S.C: O(N)
'''



# Memoization
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # Memo table
        memo = {}
          
        def solve(amount, i):
            # Lookup in memo for quick result
            if (amount, i) in memo:
                return memo[(amount, i)]
            
            # Base case: no amount can be made
            if amount == 0:
                return 0
            
            # Base case: no coins left or amount went negative
            if i >= n or amount < 0:
                return float("inf")

            # TAKE: current coin (stay at same index)
            take = float("inf")
            if amount - coins[i] >= 0:
                take = 1 + solve(amount - coins[i], i)

            # SKIP: move coin to next step
            skip = solve(amount, i + 1)

            # Return the minimum of both options
            memo[(amount, i)] = min(take, skip)
            return memo[(amount, i)]

        # If get lower coins, return it. Else return -1
        min_coins = solve(amount, 0)
        return -1 if min_coins == float("inf") else min_coins


obj = Solution()
print(obj.coinChange([1, 2, 5], 11))            # 3
print(obj.coinChange([2], 3))                   # -1
print(obj.coinChange([1], 0))                   # 0

# T.C: O(N)
# S.C: O(N)
'''



# Tabulation
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # (amount+1) ~ inf
        dp = [amount+1] * (amount+1)

        # 0 coins for 0 amount
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                # If amount doesn't become -ve
                if a - c >= 0:
                    # Without coin c
                    con1 = dp[a]

                    # With coin + pre-calculated
                    con2 = 1 + dp[a - c]

                    # Minimum number of coins
                    dp[a] = min(con1, con2)

        # Return coins if combination made else -1
        return dp[amount] if dp[amount] != amount + 1 else -1


obj = Solution()
print(obj.coinChange([1, 2, 5], 11))            # 3
print(obj.coinChange([2], 3))                   # -1
print(obj.coinChange([1], 0))                   # 0

# T.C: O(N)     --> Running loop amount times + N coins
# S.C: O(amount)     --> DP array of "amount" size used