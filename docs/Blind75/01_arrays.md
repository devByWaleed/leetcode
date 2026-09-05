# Blind 75 Part 1: Arrays

This part contains problems related to `Arrays`, `Hash-Tables`, `Two-Pointers`.

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

## 3. LeetCode 217: Contains Duplicate (Easy)

* **Identified Pattern Upfront:** Hash-Set / Sorting
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../Hashing/217.%20Contains%20Duplicate/`](../../Hashing/217.%20Contains%20Duplicate/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/contains-duplicate/submissions/2126843210)

### Code Solution

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # SORT to place duplicates side by side
        nums.sort()

        # Track 1st number
        prev = 0

        # Loop to track 2nd number and traverse
        for curr in range(1, len(nums)):
            # Duplicate condition
            if nums[curr] == nums[prev]:
                return True
            else:
                # Move pointer to check other numbers
                prev += 1

        # No duplicate found
        return False


obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))                      # True
print(obj.containsDuplicate([1, 2, 3, 4]))                      # False
print(obj.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))    # True
print(obj.containsDuplicate([2, 14, 18, 22, 22]))               # True

# T.C: O(N LOG N)       --> Looping through array + Sorting
# S.C: O(1)             --> No data structure used
```

---

## 4. LeetCode 238: Product of Array Except Self (Medium)

* **Identified Pattern Upfront:** Accumulation / Running Product
* **Time Taken:** 32 minutes
* **Solution Folder:** [`../../Arrays/238.%20Product%20of%20Array%20Except%20Self/`](../../Arrays/238.%20Product%20of%20Array%20Except%20Self/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/product-of-array-except-self/submissions/2126878559)

### Code Solution

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Static array of n length
        answer = [1] * n

        # Prefix: all elements to left
        prefix_product = 1

        # Suffix: all elements to right
        suffix_product = 1

        for i in range(n):
            # Update answer[i] with respective product
            answer[i] = answer[i] * prefix_product
            
            # Update the prefix product current index value
            prefix_product = prefix_product * nums[i]

            # Update answer[n-1-i] with respective product
            answer[n-1-i] = answer[n-1-i] * suffix_product
        
            # Update the suffix product current index value
            suffix_product = suffix_product * nums[n-1-i]

        return answer


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))          # [24, 12, 8, 6]
print(obj.productExceptSelf([-1, 1, 0, -3, 3]))     # [0, 0, 9, 0, 0]

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> As per description

# Follow up: Can you solve the problem in O(1) extra space complexity? 
# (The output array does not count as extra space for space complexity analysis.)
# ANSWER: Yes. As output array doesn't count as extra space this algorithm solves the problem in O(1) extra space complexity
```

---

## 5. LeetCode 53: Maximum Subarray (Difficulty)

* **Identified Pattern Upfront:** Running sum / MAX tracking
* **Time Taken:** 43 minutes
* **Solution Folder:** [`../../greedy/53.%20Maximum%20Subarray/`](../../greedy/53.%20Maximum%20Subarray/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/maximum-subarray/submissions/2129179589)

### Code Solution

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            # Choice 1: Creating new sub-array
            ch1 = nums[i]

            # Choice 2: Extending current window
            ch2 = curr_sum + nums[i]

            # Maximum of 2 choices
            curr_sum = max(ch1, ch2)
            
            # Updating maximum sub-array sum
            max_sum = max(max_sum, curr_sum)

        return max_sum


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))     # 6
print(obj.maxSubArray([1]))     # 1
print(obj.maxSubArray([5, 4, -1, 7, 8]))     # 23

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> No data structure used
```

---

## 6. LeetCode 152: Maximum Product Subarray (Medium)

* **Identified Pattern Upfront:** Running product / MAX tracking
* **Time Taken:** 45 minutes
* **Solution Folder:** [`../../greedy/152.%20Maximum%20Product%20Subarray/`](../../greedy/152.%20Maximum%20Product%20Subarray/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/maximum-product-subarray/submissions/2131616895)

### Code Solution

```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = max_product = min_product = nums[0]

        for i in range(1, n):
            # Negative number handling ; max_products always evaluates to higer product
            if nums[i] < 0:
                max_product, min_product = min_product, max_product


            # Minimum of 2 choices
            # Choice 1: Creating new sub-array ; Choice 2: Extending current window
            min_product = min(nums[i], min_product * nums[i])

            # Maximum of 2 choices
            # Choice 1: Creating new sub-array ; Choice 2: Extending current window
            max_product = max(nums[i], max_product * nums[i])

            ans = max(ans, max_product)

        return ans


obj = Solution()
print(obj.maxProduct([2, 3, -2, 4]))             # 6
print(obj.maxProduct([-2, 0, -1]))               # 0
print(obj.maxProduct([-2, 3, -4]))               # 24
print(obj.maxProduct([2, -5, -2, -4, 3]))        # 6

# T.C: O(N)     --> Looping through array
# S.C: O(1)     --> No data structure used
```

---

## 7. LeetCode 11: Container With Nosst Water (Difficulty)

* **Identified Pattern Upfront:** Two Pointers
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../2%20Pointers/11.%20Container%20With%20Most%20Water/`](../../2%20Pointers/11.%20Container%20With%20Most%20Water/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/container-with-most-water/submissions/2120476405)

### Code Solution

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        # calculating total water
        max_water = 0

        # 2 pointers
        left, right = 0, n - 1

        # Condition
        while left <= right:
            # Calculating total water
            # Minimum bcz we can store the water upto the minimum bar
            area = (right - left) * min(height[left], height[right])

            # Update with maximum
            max_water = max(area, max_water)

            # Move pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return max_water


obj = Solution()
print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
print(obj.maxArea([1, 1]))                       # Output: 1

# T.C: O(N)     --> Loop on N numbers
# S.C: O(1)     --> No data structure usued
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