from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Base case for small length
        if len(prices) < 2:
            return 0
        
        # 2 pointers to keep track of profit
        buy_time = 0
        sell_time = 1

        max_profit = 0      # Storing final profit


        # Condition for looping over the array
        while buy_time < sell_time and sell_time < len(prices):

            # Sell time will be greater than buy time
            if prices[sell_time] > prices[buy_time]:

                # Calculating profit
                current_profit = prices[sell_time] - prices[buy_time]

                # Updating with maximum profit
                if current_profit > max_profit:
                    max_profit = current_profit


            # Update buy time with sell time as (buy < sell)
            else:
                buy_time = sell_time

            # Incrementing for whole array traversal
            sell_time += 1
        

        return max_profit


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))     # 5
print(obj.maxProfit([7, 6, 4, 3, 1]))        # 0

# T.C: O(N)
# S.C: O(1)