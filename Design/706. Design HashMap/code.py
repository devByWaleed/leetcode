class MyHashMap:

    def __init__(self):
        # Initialize our hash-map
        self.hash_map = {}
        

    def put(self, key: int, value: int) -> None:
        # Adding / Updating value
        if key not in self.hash_map:
            self.hash_map.update({key: value})
        else:
            self.hash_map[key] = value
        

    def get(self, key: int) -> int:
        # Retrieve the value, else -1
        if key not in self.hash_map:
            return -1
        else:
            return self.hash_map[key]
        

    def remove(self, key: int) -> None:
        # Remove the mapping
        if key in self.hash_map:
            self.hash_map.pop(key)
        


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

# T.C: O(1)
# S.C: O(N)