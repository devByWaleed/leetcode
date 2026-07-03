class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_terminal = False
        

    def insert(self, word: str) -> None:
        # Get all props in curr
        curr = self

        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If the child doesn't exist, create new
            if curr.children[index] == None:
                curr.children[index] = Trie()
            
            # If child exist, move pointer to Trie instance
            curr = curr.children[index]
        
        # Marking the insertion to end
        curr.is_terminal = True
       

    def search(self, word: str) -> bool:
        # Get all props in curr
        curr = self

        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If the child doesn't exist, means word is not present
            if curr.children[index] == None:
                return False
            
            # If child exist, move pointer to Trie instance
            curr = curr.children[index]
        
        # Marking the search to end
        return curr.is_terminal
        

    def startsWith(self, prefix: str) -> bool:
        # Get all props in curr
        curr = self

        for char in prefix:
            # Get index
            index = ord(char) - ord("a")

            # If the child doesn't exist, means word is not present
            if curr.children[index] == None:
                return False
            
            # If child exist, move pointer to Trie instance
            curr = curr.children[index]
        
        # Word starts with prefix
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))   # True
print(obj.search("app"))     # False
print(obj.startsWith("app")) # True
obj.insert("app")
print(obj.search("app"))     # True

"""
None
None
True
False
True
None
True
"""