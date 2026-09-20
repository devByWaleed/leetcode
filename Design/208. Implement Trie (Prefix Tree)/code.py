class Trie:

    def __init__(self):
        # Children array
        self.children = [None] * 26
        # Indicating end of word
        self.is_terminal = False
        

    def insert(self, word: str) -> None:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                curr.children[index] = Trie()

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char, mark insertion as end
        curr.is_terminal = True


    def search(self, word: str) -> bool:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                return False

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char, mark searching as end
        return curr.is_terminal
        

    def startsWith(self, prefix: str) -> bool:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in prefix:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                return False

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char of prefix, mark searching as end
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

# T.C: O(26 • L • N) --> Looping through word and working for 26-size for each char
# S.C: insert() → O(26 • L) --> search / startsWith  → O(1)