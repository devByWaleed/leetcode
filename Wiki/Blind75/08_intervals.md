# Blind 75 Part 8: Intervals

This part contains problems related to `Intervals`

`Total Count = 5`

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

## 3. LeetCode 57: Insert Interval (Medium)

* **Identified Pattern Upfront:** Array / Intervals
* **Time Taken:** 43 minutes
* **Solution Folder:** [`../../Intervals/57.%20Insert%20Interval/`](../../Intervals/57.%20Insert%20Interval/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/insert-interval/submissions/2154626068)

### Code Solution

```python
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        
        # Track adding 
        added = False

        for i in range(len(intervals)):
            # Before newInterval
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            
            # After newInterval
            elif intervals[i][0] > newInterval[1]:
                if not added:
                    result.append(newInterval)
                    added = True
                result.append(intervals[i])
            
            # Overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # Add overlapped if don't added yet
        if not added:
            result.append(newInterval)

        return result


obj = Solution()
print(obj.insert([[1,3],[6,9]], [2,5]))                         # [[1,5],[6,9]]
print(obj.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))    # [[1,2],[3,10],[12,16]]

# T.C: O(N)     --> Looping through array
# S.C: O(N)     --> Array used for N intervals
```

---

## 4. LeetCode 56: Merge Intervals (Medium)

* **Identified Pattern Upfront:** Array / Intervals
* **Time Taken:** 25 minutes
* **Solution Folder:** [`../../Intervals/56.%20Merge%20Intervals/`](../../Intervals/56.%20Merge%20Intervals/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/merge-intervals/submissions/2154664478)

### Code Solution

```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []

        # Sorting based on .start
        intervals.sort(key=lambda x: x[0])
        

        for i in range(0, len(intervals)):
            # Overlap
            if result and intervals[i][0] <= result[-1][1]:
                # overlaps last merged interval
                result[-1][1] = max(result[-1][1], intervals[i][1])
            
            # Not overlapped
            else:
                result.append(intervals[i])

        return result


obj = Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(obj.merge([[1,4],[4,5]]))                 # [[1,5]]
print(obj.merge([[4,7],[1,4]]))                 # [[1,7]]

# T.C: O(N LOG N)       --> Sorting + Looping through array
# S.C: O(N)             --> Array used for N intervals
```

---

## 5. LeetCode 435: Non-overlapping Intervals (Medium)

* **Identified Pattern Upfront:** Array / Intervals
* **Time Taken:** 9 minutes
* **Solution Folder:** [`../../Intervals/435.%20Non-overlapping%20Intervals/`](../../Intervals/435.%20Non-overlapping%20Intervals/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/non-overlapping-intervals/submissions/2154684741)

### Code Solution

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)

        # Sorting based on .end
        intervals.sort(key=lambda x: x[1])

        # Track smallest
        last_end = -float("inf")

        count = 0        

        for i in range(0, n):
            current = intervals[i]
            
            # If tracker is smaller, update it
            if last_end <= current[0]:
                last_end = current[1]
            
            # Else add counter to skip it
            else:
                count += 1
            
        return count


obj = Solution()
print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))     # 1
print(obj.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))           # 2
print(obj.eraseOverlapIntervals([[1,2],[2,3]]))                 # 0

# T.C: O(N LOG N)       --> Sorting + Looping through array
# S.C: O(1)             --> No data structure used
```