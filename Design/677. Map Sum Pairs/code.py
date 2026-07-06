class TrieNode:
    
    def __init__(self):
        # Trie props
        self.children = {}
        self.value = 0  # To save sum for each char

class MapSum:

    def __init__(self):
        # Define root
        self.root = TrieNode()
        # Main map
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        # Calculate difference b/w existing & new value
        delta = val - self.map.get(key, 0)

        self.map[key] = val

        # Get root props
        node = self.root

        # Traverse through the Trie and add nodes
        for char in key:
            # If the child doesn't exist, create new
            if char not in node.children:
                node.children[char] = TrieNode()

            # Move pointer
            node = node.children[char]
            
            # Add delta
            node.value += delta 

    def sum(self, prefix: str) -> int:
        # Get root props
        node = self.root

        for char in prefix:
            # If the child doesn't exist, create new
            if char not in node.children:
                return 0

            node = node.children[char] 

        return node.value


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))    # return 3 (apple = 3)
obj.insert("app", 2)
print(obj.sum("ap"))    # return 5 (apple = 3)

# T.C: O(L) --> L is length of key
# S.C: O(P) --> P is length of prefix