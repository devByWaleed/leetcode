# Blind 75 Part 1: Arrays

This part contains problems related to Arrays and HashMaps.

`Total Count = 10`


## 1. LeetCode 1: Two Sum (Easy)

* **Identified Pattern Upfront:** Arrays / Hash table
* **Time Taken:** 22 minutes
* **Solution Folder:** [`../../Hashing/1.%20Two%20Sum/`](../../Hashing/1.%20Two%20Sum/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/two-sum/submissions/2125766462)

### Code Solution

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define HashMap to store difference for constant lookup
        hash_map = {}

        # Loop through the array
        for i in range(len(nums)):
            # Calculate difference = target - nums[i]
            '''
            For looking a number with current one to satisfy any condition,
            we use difference pattern (a mathematical perspective)
            '''
            difference = target - nums[i]

            # Check if difference in HashMap
            if difference in hash_map:
                # If yes then return both indices i.e., [i, HashMap[difference]]
                return [i, hash_map[difference]]

            # If no, then add {nums[i], i} to HashMap
            else:
                hash_map[nums[i]] = hash_map.get(nums[i], 0) + i

                
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(obj.twoSum([3, 2, 4], 6))        # [1, 2]
print(obj.twoSum([3, 3], 6))           # [0, 1]

# T.C: O(N)     --> Loop through N numbers array
# S.C: O(N)     --> HashMap of N numbers used
```

---

## 2. LeetCode 121: Best Time to Buy and Sell Stock (Easy)

* **Identified Pattern Upfront:** Arrays / Two Pointers
* **Time Taken:** 27 minutes
* **Solution Folder:** [`../../2%20Pointers/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/`](../../2%20Pointers/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2125804110)

### Code Solution

```python
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
```

---






## 1. LeetCode No.: Name (Difficulty)

* **Identified Pattern Upfront:** 
* **Time Taken:**  minutes
* **Solution Folder:** [`../../`](../../)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
```