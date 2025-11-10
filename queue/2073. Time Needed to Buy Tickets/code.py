from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        queue = deque()

        for i in range(len(tickets)):
            queue.append(i)

        # front is kth person -> queue[0] == k
        # while tickets[k] > 0

        return queue


obj = Solution()
print(obj.timeRequiredToBuy([2, 3, 2], 2))      # 6
print(obj.timeRequiredToBuy([5, 1, 1, 1], 0))   # 8