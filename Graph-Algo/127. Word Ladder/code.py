from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabets = {
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        }
       
        queue = deque()
        visited = set()
        word_set = set(wordList)

        # Base case
        if endWord not in word_set:
            return 0
        
        # Add starting word
        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            current_word, count = queue.popleft()

            # If we get the sequence
            if current_word == endWord:
                return count

            # For all formats of next word
            for i in range(len(current_word)):
                # For all chars in next word
                for c in alphabets:
                    # Next word formation
                    next_word = current_word[:i] + c + current_word[i+1:]

                    # If we get right word for sequence
                    if next_word in word_set and next_word not in visited:
                        queue.append((next_word, count + 1))
                        visited.add(next_word)

        return 0


obj = Solution()
print(obj.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))          # -> 5
print(obj.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # -> 0

# T.C: O(N ∗ M * 26)
# S.C: O(N ∗ M)