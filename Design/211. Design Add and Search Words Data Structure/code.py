class WordDictionary:

    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))    # False
print(obj.search("bad"))    # True
print(obj.search(".ad"))    # True
print(obj.search("b.."))    # True

'''
None
None
None
False
True
True
True
'''