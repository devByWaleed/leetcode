# Blind 75 Part 7: Intervals

This part contains problems related to `Intervals`

`Total Count = `

---

## 1. LeetCode 253: Meeting Room II (Medium)

* **Identified Pattern Upfront:** Intervals / Heap
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../Intervals/253.%20Meeting%20Rooms%20II/`](../../Intervals/253.%20Meeting%20Rooms%20II/)
* **Submittion Link:** Submitted on NeetCode

### Code Solution

```python
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
```

---

## 2. LeetCode 252: Meeting Room (Easy)

* **Identified Pattern Upfront:** Intervals / Heap
* **Time Taken:** 14 minutes
* **Solution Folder:** [`../../Intervals/252.%20Meeting%20Rooms/`](../../Intervals/252.%20Meeting%20Rooms/)
* **Submittion Link:** Submitted on NeetCode

### Code Solution

```python
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        # Edge case: No meeting or 1 meeting
        if n == 0 or n == 1:
            return True

        # Sorting based on .start
        intervals.sort(key=lambda x: x.start)

        for i in range(1, n):
            # If meeting time is in range, can't attend
            if intervals[i].start < intervals[i-1].end:
                return False

        # Can be attended
        return True


obj = Solution()
print(obj.canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))        # False
print(obj.canAttendMeetings([Interval(5,8), Interval(9,15)]))        # True

# T.C: O(N log N)   --> Sorting the given array
# S.C: O(N)         --> No data structure used
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