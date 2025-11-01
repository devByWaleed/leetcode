class MyCircularQueue:

    def __init__(self, k: int):
        pass
        

    def enQueue(self, value: int) -> bool:
        pass
        

    def deQueue(self) -> bool:
        pass
        

    def Front(self) -> int:
        pass
        

    def Rear(self) -> int:
        pass
        

    def isEmpty(self) -> bool:
        pass
        

    def isFull(self) -> bool:
        pass
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))       # True
print(obj.enQueue(2))       # True
print(obj.enQueue(3))       # True
print(obj.enQueue(4))       # True
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
True
3
True
True
True
4
"""