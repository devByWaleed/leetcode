class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        # Adding element into stack
        self.stack.append(val)
        
        # For 1st element
        if not self.min_stack:
            self.min_stack.append(val)
        
        # Compare & push
        else:
            min_num = min(self.min_stack[-1], val)
            self.min_stack.append(min_num)


    def pop(self) -> None:
        # Removing element from both stacks
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()

        
    def top(self) -> int:
        # Get top element from stack
        if self.stack:
            return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        # Top element from min_stack is minimum
        return self.min_stack[-1]
      

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