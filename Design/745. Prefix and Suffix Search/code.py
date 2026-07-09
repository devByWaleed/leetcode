from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}      # Maps character -> TrieNode
        # Save index of prefix
        self.index = -1


class WordFilter:

    def __init__(self, words: List[str]):
        # Initialize the tree with a root node
        self.root = TrieNode()
        
        for idx, w in enumerate(words):
            # i goes len + 1 to include empty suffix
            for i in range(len(w)+ 1):
                s = w[i:] + "{" + w
                self.insert(s, idx)

    def insert(self, string, index):
        curr = self.root

        for char in string:
            # If the child doesn't exist, create new
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            # Move pointer to Trie instance
            curr = curr.children[char]
            # Save index
            curr.index = index

    
    def startsWith(self, prefix):
        curr = self.root

        for char in prefix:
            # If the child doesn't exist, return -1
            if char not in curr.children:
                return -1
            
            # Move pointer to next node
            curr = curr.children[char]
        
        # Return index of prefix
        return curr.index
        

    def f(self, pref: str, suff: str) -> int:
        return self.startsWith(suff + "{" + pref)


# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(["apple"])
print(obj.f("a", "e"))

# T.C : WordFilter() -> O(L² ⋅ N) , looping through suffixes and slicing string for each word. f() -> O(P + S) , walking down prefix and suffix length
# S.C: WordFilter() -> O(L² ⋅ N) , storing maximum unique character paths inside Trie. f() -> O(1)