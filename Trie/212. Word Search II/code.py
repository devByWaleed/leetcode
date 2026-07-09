from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


obj = Solution()
print(obj.findWords(
    [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]], ["oath", "pea", "eat", "rain"]
))      # ["eat", "oath"]
print(obj.findWords(
    [["a","b"], ["c","d"]], ["abcb"]
))      # []