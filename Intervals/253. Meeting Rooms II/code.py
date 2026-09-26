from typing import List
import heapq

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)

        # Edge case: No meeting or 1 meeting
        if n == 0 or n == 1:
            return n

        min_heap = []

        # Sorting based on .start
        intervals.sort(key=lambda x: x.start)

        # Add 1st meeting by default
        heapq.heappush(min_heap, intervals[0].end)

        for i in range(1, n):
            # If meeting is over, re-use that room
            if min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)

            # Add meeting to another room
            heapq.heappush(min_heap, intervals[i].end)

        # Total rooms used
        return len(min_heap)

        
obj = Solution()
print(obj.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))        # 2
print(obj.minMeetingRooms([Interval(7, 10), Interval(2, 4)]))                  # 1
print(obj.minMeetingRooms([Interval(0, 40), Interval(5, 10), Interval(15, 20)]))        # 2
print(obj.minMeetingRooms([Interval(4, 9)]))                  # 1

# T.C: O(N LOG N)   --> Sorting by .start
# S.C: O(N)         --> Min-Heap used for N numbers