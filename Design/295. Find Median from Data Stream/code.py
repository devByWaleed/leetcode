import heapq

class MedianFinder:

    def __init__(self):
        # MAX HEAP
        self.small = []
        # MIN HEAP
        self.large = []


    def addNum(self, num: int) -> None:
        # Add to MAX HEAP firstly
        heapq.heappush(self.small, -num)

        # Maintaining order
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Maintaining length
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)


    def findMedian(self) -> float:
        # Median of odd size
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # Median of even size
        return (-self.small[0] + self.large[0]) / 2
        

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


# Brute Force
"""
class MedianFinder:

    def __init__(self):
        self.array = []
        
        '''
        Maintaining a dynamic data stream to efficiently calculate the median without re-sorting all elements every time.

        Suggestions:
            Consider avoiding full sorts in addNum to improve efficiency and reduce nested logic complexity.
        '''

    def addNum(self, num: int) -> None:
        # heapq.heappush(self.array, num)
        self.array.append(num)
        self.array.sort()
        

    def findMedian(self) -> float:
        if len(self.array) % 2 == 0:
            num2 = self.array[len(self.array) // 2]
            num1 = self.array[(len(self.array) // 2) - 1]

            median = (num1 + num2) / 2
        else:
            median = self.array[len(self.array) // 2]
        
        return float(median)
        

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()

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
# Output:
'''
None
None
None
1.5
None
2.0
'''


# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())     # 1.5
# obj.addNum(3)
# print(obj.findMedian())     # 2.0
# Output:
'''
None
None
None
1.5
None
2.0
'''
"""