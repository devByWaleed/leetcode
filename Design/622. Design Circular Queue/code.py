class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * self.k
        self.front_element = -1
        self.rear_element = -1
        self.counter = 0


    def enQueue(self, value: int) -> bool:

        # Checking if queue is full or not
        if self.counter == self.k:
            return False

        # If queue is not full, then we can add the element
        if self.front_element == -1:
            self.front_element = 0

        # Adding element and incrementing check counter
        self.rear_element = (self.rear_element + 1) % self.k
        self.queue[self.rear_element] = value
        self.counter += 1
        return True


    def deQueue(self) -> bool:

        # Check for empty queue
        if self.counter == 0:
            return False

        # Check that queue has 1 element
        if self.front_element == self.rear_element:
            self.front_element = -1
            self.rear_element = -1
        # Move front element
        else:
            self.front_element = (self.front_element + 1) % self.k

        # Operation successful
        self.counter -= 1
        return True


    def Front(self) -> int:
        # Check for empty queue
        if self.counter == 0:
            return -1
        else:
            return self.queue[self.front_element]


    def Rear(self) -> int:
        # Check for empty queue
        if self.counter == 0:
            return -1
        else:
            return self.queue[self.rear_element]


    def isEmpty(self) -> bool:
        # counter == 0, means queue is empty
        return self.counter == 0

    
    def isFull(self) -> bool:
        # counter == k, means queue is full
        return self.counter == self.k



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

# T.C: O(1)
# S.C: O(K)