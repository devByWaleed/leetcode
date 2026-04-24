from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Define Heap
        self.k = k
        self.min_heap = nums.copy()

        # Create MIN HEAP
        heapq.heapify(self.min_heap)

        # POP elements not in k range
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        # Push value
        heapq.heappush(self.min_heap, val)

        # If elements becomes larger than k, POP minimum element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return kth largest element
        return self.min_heap[0]
          

# Your KthLargest object will be instantiated and called as such:
obj1 = KthLargest(3, [4, 5, 8, 2])

print(obj1.add(3))     # 4
print(obj1.add(5))     # 5
print(obj1.add(10))    # 5
print(obj1.add(9))     # 8
print(obj1.add(4))     # 8
# Output:
'''
None
4
5
5
8
8
'''

obj2 = KthLargest(4, [7, 7, 7, 7, 8, 3])

print(obj2.add(2))     # 7
print(obj2.add(10))    # 7
print(obj2.add(9))     # 7
print(obj2.add(9))     # 8
# Output:
'''
None
7
7
7
8
'''

# T.C: O(N LOG N) / O(N) -> __init__ | O(LOG K) -> add()
# S.C: O(K)