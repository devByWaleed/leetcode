# Blind 75 Part 6: Heap

This part contains problems related to `Heap`

`Total Count = 2`

---

## 1. LeetCode 347: Top K Frequent Elements (Medium)

* **Identified Pattern Upfront:** Hash-Tables / Heap
* **Time Taken:** 26 minutes
* **Solution Folder:** [`../../Hashing/347.%20Top%20K%20Frequent%20Elements/`](../../Hashing/347.%20Top%20K%20Frequent%20Elements/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/top-k-frequent-elements/submissions/2153499337)

### Code Solution

```python
# HashMap + Min-Heap

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Store frequencies
        frequencies = {}

        # MinHeap for Top K, result for final answer
        min_heap, result = [], []

        # 1: Store frequencies
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1

        # 2: Update MinHeap with Top K Frequent elements
        for num, frequency in frequencies.items():
            heapq.heappush(min_heap, (frequency, num))

            # If size exceeded, remove smallest one
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 3: Add the actual number to result
        for pair in min_heap:
            result.append(pair[1])

        return result


obj = Solution()
print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))       # [1, 2]
print(obj.topKFrequent([1], 1))                      # [1]
print(obj.topKFrequent([3, 0, 1, 0], 1))             # [0]

# T.C: O(N log K)   --> Main MinHeap of K elements for N total numbers
# S.C: O(N)         --> MinHeap + result array used
```

---

## 2. LeetCode 295: Find Median from Data Stream (Hard)

* **Identified Pattern Upfront:** Heap
* **Time Taken:** 49 minutes
* **Solution Folder:** [`../../Design/295.%20Find%20Median%20from%20Data%20Stream/`](../../Design/295.%20Find%20Median%20from%20Data%20Stream/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/find-median-from-data-stream/submissions/2153542848)

### Code Solution

```python
import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        # ADD to MAX-Heap first
        heapq.heappush(self.max_heap, -num)

        # MAX-Heap's largest <= MIN-Heap's smallest 
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Balancing length
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
        
    def findMedian(self) -> float:
        # ODD count
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        
        # EVEN count
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()

obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())     # 1.5
obj.addNum(3)
print(obj.findMedian())     # 2.0
# Output:
'''
None
None
None
1.5
None
2.0
'''

obj.addNum(6)
print(obj.findMedian())     # 6.00000
obj.addNum(10)
print(obj.findMedian())     # 8.00000
obj.addNum(2)
print(obj.findMedian())     # 6.00000
obj.addNum(6)
print(obj.findMedian())     # 6.00000
obj.addNum(5)
print(obj.findMedian())     # 6.00000
obj.addNum(0)
print(obj.findMedian())     # 5.50000
obj.addNum(6)
print(obj.findMedian())     # 6.00000
obj.addNum(3)
print(obj.findMedian())     # 5.50000
obj.addNum(1)
print(obj.findMedian())     # 5.00000
obj.addNum(0)
print(obj.findMedian())     # 4.00000
obj.addNum(0)
print(obj.findMedian())     # 3.00000

# T.C: O(LOG N) -> addNum() | O(1) -> findMedian()
# S.C: O(N)
```