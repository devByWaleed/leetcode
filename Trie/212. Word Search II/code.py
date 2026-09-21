from typing import List

class TrieNode:
    def __init__(self):
        # Children array
        self.children = [None] * 26
        # Indicating end of word
        self.word = None

    def insert(self, words):
        
        for i in range(len(words)):
            curr = self
            word = words[i]
            for j in range(len(word)):
                # Get index
                index = ord(word[j]) - ord("a")

                # If child doesn't exists, create new one
                if not curr.children[index]:
                    curr.children[index] = TrieNode()

                # If exists, move pointer to it's children
                curr = curr.children[index]

            # After last char, mark insertion as end
            curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        # Final answer array
        result = []

        trieNode = TrieNode()
        trieNode.insert(words)

        def dfs(r, c, node):
            # Edge cases: Out of bound + visited
            # if (r < m and r >= m and c < n and c >= n) or board[r][c]:
            if (r < 0 or c < 0 or r >= m or c >= n) or board[r][c] == "#":
                return

            # Get index
            index = ord(board[r][c]) - ord("a")

            # If not present
            if not node.children[index]:
                return

            # Pointer for traversal
            curr = node.children[index]

            # If word found in TrieNode, add it to result
            if curr.word:
                result.append(curr.word)
                # Mark as None
                curr.word = None

            # Storing in temp + marking as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Recursive call on all 4 directions :DOWN, UP, RIGHT, LEFT
            dfs(r+1, c, curr)
            dfs(r-1, c, curr)
            dfs(r, c+1, curr)
            dfs(r, c-1, curr)

            # UNDO: Place original character
            board[r][c] = temp


        # Passing i,j to dfs()
        for i in range(m):
            for j in range(n):
                dfs(i, j, trieNode)

        return result


obj = Solution()
print(obj.findWords(
    [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]], ["oath", "pea", "eat", "rain"]
))      # ["eat", "oath"]
print(obj.findWords(
    [["a","b"], ["c","d"]], ["abcb"]
))      # []

# T.C: O(M ∗ N ∗ 4^L)   --> Nested looping on grid + checking 4 directions for L length word
# T.C: O(S)             --> Trie + result array