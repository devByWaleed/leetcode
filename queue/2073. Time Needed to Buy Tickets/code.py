from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0     # To track time

        for index, t_needed in enumerate(tickets):

            # Front of k: They will buy at most tickets[k]
            if index <= k:
                time += min(t_needed, tickets[k])

            # Behind of k: They will buy at most tickets[k] - 1
            else:
                time += min(tickets[index], tickets[k] - 1)
        

        return time


obj = Solution()
print(obj.timeRequiredToBuy([2, 3, 2], 2))      # 6
print(obj.timeRequiredToBuy([5, 1, 1, 1], 0))   # 8

# T.C: O(N)
# S.C: O(1)




# Brute Force
'''
from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        time = 0     # To track time

        # Make queue of tickets with index
        for i in range(len(tickets)):
            queue.append((i, tickets[i]))


        while True:
            index, t_needed = queue.popleft()
            t_needed -= 1
            time += 1
            
            # If kth person has buy all tickets
            if index == k and t_needed == 0:
                break

             # If ticket has to buy
            if t_needed > 0:
                queue.append((index, t_needed))


        return time


obj = Solution()
print(obj.timeRequiredToBuy([2, 3, 2], 2))      # 6
print(obj.timeRequiredToBuy([5, 1, 1, 1], 0))   # 8

# T.C: O(N * M)
# S.C: O(N)
'''