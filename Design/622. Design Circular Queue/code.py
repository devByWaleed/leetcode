from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        # self.queue = []
        self.queue = [0] * self.k
        self.front_element = -1
        self.rear_element = -1
        self.counter = 0 
        # self.queue = deque(self.queue)
        

    def enQueue(self, value: int) -> bool:
        if self.counter == self.k:
            return False


        if (self.rear_element + 1) % self.k == self.front_element:
            (self.front_element + 1) % self.k

        elif self.front_element == -1:
            self.front_element = 0
        
        self.rear_element = (self.rear_element + 1) % self.k
        self.queue[self.rear_element] = value
        self.counter += 1
        return True
        

    def deQueue(self) -> bool:
        if self.front_element == -1:
            return False
        
        result = self.queue[self.front_element]

        if self.front_element == self.rear_element:
            self.front_element = -1
            self.rear_element = -1
        else:
            self.front_element = (self.front_element + 1) % self.k

        return True
        

    def Front(self) -> int:
        if self.front_element == -1:
            return -1
        else:
            return self.queue[0]
            # return self.queue[self.front_element]
        

    def Rear(self) -> int:
        if self.front_element == -1:
            return -1
        else:
            return self.queue[len(self.queue)-1]
            # return self.queue[self.rear_element]
        
        
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        

    def isFull(self) -> bool:
        return len(self.queue) != 0
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))       # True
print(obj.enQueue(2))       # True
print(obj.enQueue(3))       # True
print(obj.enQueue(4))       # False
print(obj.Rear())           # 3
print(obj.isFull())         # True
print(obj.deQueue())        # True
print(obj.enQueue(4))       # True
print(obj.Rear())           # 4

"""
None
True
True
True
False
3
True
True
True
4
"""