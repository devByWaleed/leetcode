# Contest 1: Weekly-Contest-523

This file contains all the problem's solution and Link for Weekly-Contest-523


## 1. LeetCode 4078: Three Fibonacci Sum (Easy)

* **Identified Pattern Upfront:** Two Pointers
* **Time Taken:** 
* **Solution Folder:** [`../../Two-Pointers/4450.%20Three%20Fibonacci%20Sum/`](../../Two-Pointers/4450.%20Three%20Fibonacci%20Sum/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/three-fibonacci-sum/submissions/2172652496)

### Code Solution

```python
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        l, r = 0, 1
        sum_3 = l + r

        while (sum_3 + r + l) <= n:
            if (sum_3 + r + l) == n:
                return True
            else: 
                l = r
                r = sum_3
                sum_3 = l + r
        
        return False
        

obj = Solution()
print(obj.threeFibonacciSum(16))
print(obj.threeFibonacciSum(8))
print(obj.threeFibonacciSum(2))

# T.C:  O(N)    --> Loop through ~ N times
# S.C:  O(1)    --> No data structure used

```

---

## 2. LeetCode 4079: Prime Subset Selection I (Medium)

* **Identified Pattern Upfront:** Array
* **Time Taken:** 
* **Solution Folder:** [`../../Arrays/4433.%20Prime%20Subset%20Selection%20I/`](../../Arrays/4433.%20Prime%20Subset%20Selection%20I/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/prime-subset-selection-i/submissions/2172682062)

### Code Solution

```python
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        def get_prime(n):
            # boolean list tracking potential primes
            is_prime = [True] * (n + 1)

            # Mark 0 and 1 as non-prime
            is_prime[0] = is_prime[1] = False

            # Loop up to the square root of n
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            # Final list
            return [num for num, prime in enumerate(is_prime) if prime]

        prime_list = get_prime(n)

        # Get the prime number window
        total = 0
        count = 0
        for num in prime_list:
            # count sum
            total += num

            # If sum exceeded, break
            if total > s:
                break

            # If sum is in range, increase window
            count += 1

        # Return array of specific range
        return prime_list[0:count]
        

obj = Solution()
print(obj.maxPrimes(7))
print(obj.maxPrimes(20))
print(obj.maxPrimes(15))
print(obj.maxPrimes(15))
print(obj.maxPrimes(5))
print(obj.maxPrimes(1))

# T.C:  O(N)    --> checking for prime numbers + counting
# S.C:  O(N)    --> Array used for N numbers
```

---

## 3. LeetCode 4080: Design Bus Seat Booking System (Medium)

* **Identified Pattern Upfront:** Design / Array
* **Time Taken:** 
* **Solution Folder:** [`../../Design/4377.%20Design%20Bus%20Seat%20Booking%20System/`](../../Design/4377.%20Design%20Bus%20Seat%20Booking%20System/)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
from typing import List

class BusBooking:

    def __init__(self, n: int):
        self.system = []
        self.map = {
            "A": 1, "B": 2,
            "C": 3, "D": 4
        }
        
        for i in range(n):
            self.system.append([])
            for j in range(1, 5):
                self.system[i].append(False)
        

    def toggle(self, seat: str) -> None:
        row_num = int(seat[1:])
        total_time = 0

        if seat[0] == "B" or seat[0] == "C":
            if not self.system[row_num][self.map[seat[0]]]:
                total_time += 1
        else:
            if not adjacent_seat_checking:
                total_time += 1
            else:
                total_time += 3
        

    def getTotalTime(self) -> int:
        pass
        

    def getMinTime(self) -> int:
        pass
        


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()

obj = BusBooking()
print(obj.__init__(["BusBooking","toggle","toggle","getTotalTime","getMinTime","toggle","toggle","getTotalTime","getMinTime"]))
print(obj.__init__([[20],["B3"],["A3"],[],[],["C3"],["D3"],[],[]]))
print(obj.__init__(["BusBooking","toggle","toggle","getTotalTime","toggle","toggle","toggle","getTotalTime","getMinTime"]))
print(obj.__init__([[10],["C7"],["D7"],[],["D7"],["C7"],["D7"],[],[]]))

# T.C:  O()
# S.C:  O()
```