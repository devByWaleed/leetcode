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


'''
- Create dp array of size (amount+1) with amount+1 as default value
- Set dp[0] to 0
- Loop through 1 to amount+1 with a
    - Loop through all coins with c
        - if a - c >= 0:
            - Condition 1: Without coin ==> Save dp[a] in con1
            - condition 2: With coin ==> Save 1 + dp[a - c] in con2
            - Update dp[a] with min(con1, con2)
- At the end, if dp[amount] != amount + 1, return dp[amount] as miinimum coin needed. Else return -1
'''