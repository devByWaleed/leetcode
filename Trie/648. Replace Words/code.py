from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}      # Maps character -> TrieNode
        self.is_terminal = False  # Marks the end of a valid word


class Solution:
    def __init__(self):
        # Initialize the tree with a root node
        self.root = TrieNode()

    def createTrie(self, root_word):
        # Pointer
        curr = self.root

        for char in root_word:
            # If the character path doesn't exist, create it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            # Moving down selected character branch
            curr = curr.children[char]
        
        # Mark the end of the word
        curr.is_terminal = True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Building Trie
        for root_word in dictionary:
            self.createTrie(root_word)
        
        # Splitting into array
        sen_arr = sentence.split(" ")


        for i in range(len(sen_arr)):
            # Pointer in outer loop for correct position tracking
            curr = self.root
            # Single word which will place in
            prefix = ""
            for char in sen_arr[i]:
                # If a character is missing, the exact word doesn't exist
                if char not in curr.children:
                    break
                else:
                    curr = curr.children[char]
                    prefix += char

                    # If Trie word ends
                    if curr.is_terminal:
                        sen_arr[i] = prefix
                        break
                
        # Making final string
        ans = " ".join(sen_arr)
        return ans


obj = Solution()
print(obj.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))      # "the cat was rat by the bat"
print(obj.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))      # "a a b c"

# T.C: O(d×l + s×l)
# S.C: O(d×l + s)