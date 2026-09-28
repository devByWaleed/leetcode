# Blind 75 Part 9: Bit-Manipulation

This part contains problems related to `Bitwise`

`Total Count = 5`

---

## 1. LeetCode 191: Number of 1 Bits (Easy)

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

## 2. LeetCode 338: Counting Bits (Easy)

* **Identified Pattern Upfront:** Bit-Manipulation / DP
* **Time Taken:** 21 minutes
* **Solution Folder:** [`../../Bit-Manipulation/338.%20Counting%20Bits/`](../../Bit-Manipulation/338.%20Counting%20Bits/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/counting-bits/submissions/2155687037)

### Code Solution

```python
# DP Approach
class Solution:
    def countBits(self, n: int) -> List[int]:       
        # DP Array for final answer
        ans = [0] * (n+1)

        for i in range(1, n+1):
            # add bit count + signal for even/odd
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


obj = Solution()
print(obj.countBits(2))      # [0, 1, 1]
print(obj.countBits(5))      # [0, 1, 1, 2, 1, 2]

# T.C: O(N)     --> Looping + constant bit-operation through N times
# S.C: O(N)     --> DP array of size N used
```

## 3. LeetCode 268: Missing Number (Easy)

* **Identified Pattern Upfront:** Math / Bitwise
* **Time Taken:** 4 minutes
* **Solution Folder:** [`../../Bit-Manipulation/268.%20Missing%20Number/`](../../Bit-Manipulation/268.%20Missing%20Number/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/missing-number/submissions/2155705122)

### Code Solution

```python
# XOR operator
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        xor_array = 0
        xor_range = 0

        # XORing the array numbers
        for num in nums:
            xor_array = xor_array ^ num

        # XORing the range numbers
        for i in range(n+1):
            xor_range = xor_range ^ i

        # Xoring number itself cancel out
        return xor_array ^ xor_range
    

obj = Solution()

print(obj.missingNumber([3, 0, 1]))                     # 2
print(obj.missingNumber([0, 1]))                        # 2
print(obj.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))   # 8

# T.C = O(N)    --> XORing N numbers
# S.C = O(1)    --> No data structure used
```

---

## 4. LeetCode 190: Reverse Bits (Easy)

* **Identified Pattern Upfront:** Bitwise
* **Time Taken:** 4 minutes
* **Solution Folder:** [`../../Bit-Manipulation/190.%20Reverse%20Bits/`](../../Bit-Manipulation/190.%20Reverse%20Bits/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/reverse-bits/submissions/2155714351)

### Code Solution

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_bit = 0
        num = n

        for _ in range(32):
            # Merged = (Shifting bit for allocating space) + LSB
            reverse_bit = (reverse_bit << 1) | (num & 1)

            # Discard LSB we get earlier
            num = num >> 1

        return reverse_bit


obj = Solution()
print(obj.reverseBits(43261596))      # 964176192
print(obj.reverseBits(2147483644))      # 1073741822

# T.C: O(1)     --> Looping 32 times (constant)
# S.C: O(1)     --> No data structure used
```

---

## 5. LeetCode 371: Sum of Two Integers (Medium)

* **Identified Pattern Upfront:** Bitwise
* **Time Taken:**  minutes
* **Solution Folder:** [`../../Bit-Manipulation/371.%20Sum%20of%20Two%20Integers/`](../../Bit-Manipulation/371.%20Sum%20of%20Two%20Integers/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/sum-of-two-integers/submissions/2155733347)

### Code Solution

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask of 32-bit to handle Python's integer
        mask = 0xFFFFFFFF
        
        # Save copy
        num1, num2 = a & mask, b & mask
        
        #while num2 != 0:
        while num1 != 0:
            # Save carry for bigger numbers
            carry = (num1 & num2) & mask
            
            # XOR done sum without carry
            #num1 = (num1 ^ num2) & mask
            num2 = (num1 ^ num2) & mask
            
            # Shift carry by 1 and store it for later sum
            #num2 = (carry << 1) & mask
            num1 = (carry << 1) & mask
         
        # If number is -ve, convert num2 back to -ve
        if num2 > 0x7FFFFFFF:
            return ~(num2 ^ mask)
            
        return num2
        #return num1


obj = Solution()
print(obj.getSum(1, 2))     # 3
print(obj.getSum(2, 3))     # 5

# T.C: O(1)     --> Looping is constant
# S.C: O(1)     --> No data structure used
```