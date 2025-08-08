class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence) == 1:      return True


obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))    # True
print(obj.checkIfPangram("leetcode"))                               # False