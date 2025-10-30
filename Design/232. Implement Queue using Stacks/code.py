class MyQueue:

    def __init__(self):
        self.main = []
        self.outer = []
        

    def push(self, x: int) -> None:
        self.main.append(x)
        

    def pop(self) -> int:
        if not self.outer:
            while self.main:
                top = self.main.pop()
                self.outer.append(top)
        
        return self.outer.pop()
        

    def peek(self) -> int:
        if not self.outer:
            while self.main:
                top = self.main.pop()
                self.outer.append(top)
        
        return self.outer[len(self.outer)-1]
        

    def empty(self) -> bool:
        return len(self.main) == 0 and len(self.outer) == 0
        

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())       # 1
print(obj.pop())        # 1
print(obj.empty())      # False

"""
None
None
None
1
1
False
"""

# T.C: O(1) Amortized For Push,Pop,Peek, And O(1) For Empty
# S.C: O(N)