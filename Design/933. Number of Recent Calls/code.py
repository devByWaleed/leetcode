from collections import deque

class RecentCounter:

    def __init__(self):
        # Initialize queue
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        
        # Adding request to queue
        self.queue.append(t)

        # If current request is greater than 1st reuest, remove 1st element
        while self.queue and t - 3000 > self.queue[0]:
            self.queue.popleft()

        # Queue size will dynamically track no. of requests
        return len(self.queue)
        

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))      # 1
print(obj.ping(100))    # 2
print(obj.ping(3001))   # 3
print(obj.ping(3002))   # 3

"""
None
1
2
3
3
"""

# T.C: O(1)
# S.C: O(N)