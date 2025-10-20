class MinStack:

    def __init__(self):
        self.st = []
        self.min_value = []
        self.n = len(self.st)
        self.m = len(self.min_value)
        

    def push(self, val: int) -> None:
        self.st.append(val)
        
        # Adding value to 2nd stack
        if not self.min_value or val <= self.min_value[self.m-1]:
            self.min_value.append(val)
        

    def pop(self) -> None:
        # If equal, pop from both, else pop from main stack
        if self.st[self.n-1] == self.min_value[self.m-1]:
            self.st.pop()
            self.min_value.pop()
        else:
            self.st.pop()
        

    def top(self) -> int:
        # Top element of main stack
        if self.st:
            return self.st[self.n-1]
        

    def getMin(self) -> int:
        # Top element of 2nd stack
        if self.min_value:
            return self.min_value[self.m-1]
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())     # -3
obj.pop()
print(obj.top())        # 0
print(obj.getMin())     # -2

# Output:
'''
None
None
None
None
-3
None
0
-2
'''

# T.C: O(1)
# S.C: O(N)