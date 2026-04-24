from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Edge case for 1 stone
        if len(stones) == 1:
            return stones[0]
        
        # Create MAX HEAP
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # Terminate condition
        while len(max_heap) != 1:
            # 1st largest stone
            y = heapq.heappop(max_heap)
            # 2nd largest stone
            x = heapq.heappop(max_heap)

            if x != y:
                # Update y
                y = y - x
                # Add to heap & heapify
                heapq.heappush(max_heap, y)
            else:
                # If stones destroyed
                if len(max_heap) == 0:
                    return 0

        # Final stone left in heap
        return -max_heap[0]


obj = Solution()
print(obj.lastStoneWeight([2, 7, 4, 1, 8, 1]))   # 1
print(obj.lastStoneWeight([1]))   # 1
print(obj.lastStoneWeight([2, 2]))   # 0

# T.C: O(N LOG N)
# S.C: O(N)