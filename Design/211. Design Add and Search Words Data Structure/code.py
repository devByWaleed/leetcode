class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.is_terminal = False

    def addWord(self, word: str) -> None:
        # Get all props in curr
        curr = self

        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If the child doesn't exist, create new
            if curr.children[index] == None:
                curr.children[index] = WordDictionary()

            # If child exist, move pointer to Trie instance
            curr = curr.children[index]
        
        # Marking the insertion to end
        curr.is_terminal = True

    def search(self, word: str) -> bool:
        # Set to keep track of all possible Trie nodes
        current_nodes = {self}  # Start with root
        
        for char in word:
            # This set will collect all valid next states for the upcoming character
            next_nodes = set()
            
            for node in current_nodes:
                # Handling wildcard
                if char == ".":
                    # Loop through all 26 possibilities
                    for child in node.children:
                        # If a branch exists for this letter, it's a valid path
                        if child:
                            next_nodes.add(child)
                
                # Handling letters
                else:
                    index = ord(char) - ord("a")
                    if node.children[index]:
                        next_nodes.add(node.children[index])
            
            # If no valid paths exist for this character, stop early and return False.
            if not next_nodes:
                return False
            
            # Move to next layer
            current_nodes = next_nodes
        
        # Check if any node is terminal
        return any(node.is_terminal for node in current_nodes)



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