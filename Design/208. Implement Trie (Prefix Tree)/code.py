class Trie:

    def __init__(self):
        pass
        

    def insert(self, word: str) -> None:
        pass
        

    def search(self, word: str) -> bool:
        pass
        

    def startsWith(self, prefix: str) -> bool:
        pass
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.search("apple")   # True
obj.search("app")     # False
obj.startsWith("app") # True
obj.insert("app")
obj.search("app")     # True

"""
None
None
True
False
True
None
True
"""