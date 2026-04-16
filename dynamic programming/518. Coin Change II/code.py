from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # Memo table
        memo = {}
          
        def solve(i, a):
            # Lookup in memo for quick result
            if (i, a) in memo:
                return memo[(i, a)]
            
            # Base case: we get amount from that coin
            if a == amount:
                return 1
            
            # Base case: we get bigger amount from that coin
            if a > amount:
                return 0
            
            # Base case: we check all coins
            if i >= n:
                return 0
            
            # TAKE: current coin (stay at same index)
            take = solve(i, a + coins[i])

            # SKIP: move coin to next step
            skip = solve(i + 1, a)
            
            memo[(i, a)] = take + skip
            return memo[(i, a)]
        
        return solve(0, 0)
       

obj = Solution()
print(obj.change(5, [1, 2, 5]))             # 4
print(obj.change(3, [2]))                   # 0
print(obj.change(10, [10]))                 # 1

# T.C: O(N)
# S.C: O(N)