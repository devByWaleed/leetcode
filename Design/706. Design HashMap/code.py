class MyHashMap:

    def __init__(self):
        pass
        

    def put(self, key: int, value: int) -> None:
        pass
        

    def get(self, key: int) -> int:
        pass
        

    def remove(self, key: int) -> None:
        pass
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))       # 1
print(obj.get(3))       # -1
obj.put(2, 1)
print(obj.get(2))       # 1
obj.remove(2)
print(obj.get(2))       # -1

# Output:
'''
None
None
None
1
-1
None
1
None
-1
'''