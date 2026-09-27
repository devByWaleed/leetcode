# Blind 75 Part 9: Bit-Manipulation

This part contains problems related to `Intervals`

`Total Count = 5`

---

## 1. LeetCode  (Easy)

* **Identified Pattern Upfront:** Bit-Manipulation
* **Time Taken:** 6 minutes
* **Solution Folder:** [`../../Bit-Manipulation/191.%20Number%20of%201%20Bits/`](../../Bit-Manipulation/191.%20Number%20of%201%20Bits/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/number-of-1-bits/submissions/2154700186)

### Code Solution

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
       # Total set bits
        count = 0

        num = n

        while num > 0:
            # Checking 1 bit
            num = num & (num-1)

            # Increment count
            count += 1
        
        return count


obj = Solution()
print(obj.hammingWeight(11))            # 3
print(obj.hammingWeight(128))           # 1
print(obj.hammingWeight(2147483645))    # 30

# T.C: O(K)     --> Number of set bits
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