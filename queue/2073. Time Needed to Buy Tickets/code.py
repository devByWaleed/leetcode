from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        counter = 0     # To track time

        # Make queue of index,tickets
        for i in range(len(tickets)):
            queue.append((i,tickets[i]))


        while True:
            person = queue.popleft()
            curr = person[1]
            curr -= 1

            # If ticket has to buy
            if curr > 0:
                new = (person[0], curr)
                queue.append(new)
                counter += 1

            # If kth person has buy all tickets
            elif person[0] == k and curr == 0:
                break
            # If other person has bought all tickets
            else:
                counter += 1
                continue
            
        return counter+1


obj = Solution()
print(obj.timeRequiredToBuy([2, 3, 2], 2))      # 6
print(obj.timeRequiredToBuy([5, 1, 1, 1], 0))   # 8

# T.C: O(N * M)
# S.C: O(N)