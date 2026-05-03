from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort by starti
        meetings.sort()

        # Free Heap
        available = [i for i in range(0, n)]

        # Busy Heap
        used = []

        # Keep track of maximum meetings by every room
        count = [0] * n

        for start, end in meetings:
            # Finish meeting
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # If no room available
            if not available:
                endi, room = heapq.heappop(used)
                end = endi + (end - start)
                heapq.heappush(available, room)

            # Using available room
            room = heapq.heappop(available)
            heapq.heappush(used, [end, room])

            # Current room get 1 meeting
            count[room] += 1

        # Return room conducts maximum meetings
        return count.index(max(count))


obj = Solution()
print(obj.mostBooked(2, [[0,10], [1,5], [2,7], [3,4]]))             # 0
print(obj.mostBooked(3, [[1,20], [2,10], [3,5], [4,9], [6,8]]))     # 1

# T.C: O(M LOG M + M LOG N)
# S.C: O(M LOG M + M LOG N)