from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Edge case
        if len(intervals) == 1:
            return 1
        
        # Sort by starti
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        # Define Heap
        min_heap = []
        
        # Add 1st room manually & heapify
        min_heap.append(sorted_intervals[0][1])
        heapq.heapify(min_heap)

        for i in range(1, len(sorted_intervals)):
            # Get starti, endi
            starti = sorted_intervals[i][0]
            endi = sorted_intervals[i][1]

            # If true, means meeting has ended
            if starti >= min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, endi)
            # Means meeting isn't done yet
            else:
                heapq.heappush(min_heap, endi)

        # No. of conference rooms
        return len(min_heap)


obj = Solution()
print(obj.minMeetingRooms([[0,30], [5,10], [15,20]]))        # 2
print(obj.minMeetingRooms([[7,10], [2,4]]))                  # 1

# T.C: O(N LOG N)
# S.C: O(N)