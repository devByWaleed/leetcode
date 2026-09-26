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