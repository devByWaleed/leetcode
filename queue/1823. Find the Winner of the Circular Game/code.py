from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = []
        # queue = deque()
        count = 0

        for i in range(1, n+1):
            queue.append(i)


        while len(queue) != 1:

            count = (count + k) % len(queue) - 1
            queue.pop(count)
  

        return queue[0]


obj = Solution()
print(obj.findTheWinner(5, 2))      # 3
print(obj.findTheWinner(6, 5))      # 1