from collections import deque

class MyStack:

    def __init__(self):
        self.main = deque()
        self.outer = deque()
        

    def push(self, x: int) -> None:
        self.outer.append(x)

        while self.main:
            self.outer.append(self.main.popleft())

        self.main, self.outer = self.outer, self.main


    def pop(self) -> int:
        return self.main.popleft()
        

    def top(self) -> int:
        return self.main[0]
        

    def empty(self) -> bool:
        return len(self.main) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())        # 2
print(obj.pop())        # 2
print(obj.empty())      # False

"""
None
None
None
2
2
False
"""

# T.C: O(N)
# S.C: O(N)