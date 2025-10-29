from collections import deque

class MyQueue:

    def __init__(self):
        self.st = deque()
        

    def push(self, x: int) -> None:
        self.st.append(x)
        

    def pop(self) -> int:
        top = self.st.popleft()
        return top
        

    def peek(self) -> int:
        return self.st[0]
        

    def empty(self) -> bool:
        return len(self.st) == 0
        

# # Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)
# print(obj.peek())       # 1
# print(obj.pop())        # 1
# print(obj.empty())      # False

"""
None
None
None
1
1
False
"""


# Using 2 stacks
'''
class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        self.st1.append(x)
        

    def pop(self) -> int:
        top = self.st1.pop()
        self.st2.append(top)
        return self.st1[0]
        

    def peek(self) -> int:
        return self.st1[0]
        

    def empty(self) -> bool:
        return len(self.st1) == 0
        

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.peek())       # 1
print(obj.pop())        # 1
print(obj.pop())        # 1
print(obj.peek())       # 1
print(obj.empty())      # False

"""
None
None
None
1
1
False
"""
'''