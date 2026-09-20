class WordDictionary:

    def __init__(self):
        # Children array
        self.children = [None] * 26
        # Indicating end of word
        self.is_terminal = False


    def addWord(self, word: str) -> None:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                curr.children[index] = WordDictionary()

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char, mark insertion as end
        curr.is_terminal = True


    def search(self, word: str) -> bool:
        def dfs(i, node):
            # Pointer for traversal
            curr = node

            for j in range(i, len(word)):
                # Current word
                char = word[j]

                # WILDCARD case
                if char == ".":
                    for child in curr.children:
                        # If child, recursively check for rest of branch
                        if child and dfs(j+1, child):
                            return True

                    return False

                # Standard letter
                else:
                    # Get index
                    index = ord(char) - ord("a")
        
                    # If child doesn't exists, create new one
                    if not curr.children[index]:
                        return False
        
                    # If exists, move pointer to it's children
                    curr = curr.children[index]
        
            # After last char, mark searching as end
            return curr.is_terminal

        return dfs(0, self)

    
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

# obj.addWord("a")
# obj.addWord("a")
# print(obj.search("."))    # True
# print(obj.search("a"))    # True
# print(obj.search("aa"))    # False
# print(obj.search("a"))    # True
# print(obj.search(".a"))    # False
# print(obj.search("a."))    # False

'''
None
None
True
True
False
True
False
False
'''

# T.C: addWord() --> O(L) || search() --> Wildcard:Worst-case O(26^d * L), No Wild-card:O(L)
# S.C: O(N * L)