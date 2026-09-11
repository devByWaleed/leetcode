from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Define Two pointers to check stocks
        buy, sell = 0, 1

        # max_profit stores maximum profit
        max_profit = 0

        # Looping through array
        while sell < n:
            # If profit of sell day < profit of buy, update buy to skip it
            if prices[sell] < prices[buy]:
                buy = sell

            # If profit is greater, update max_profit
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

            # Update sell for iteration
            sell += 1

        # At the end, return maximum profit
        return max_profit

        
obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))     # 5
print(obj.maxProfit([7, 6, 4, 3, 1]))        # 0

# T.C: O(N)     --> Looping through N numbers array
# S.C: O(1)     --> No data structure used