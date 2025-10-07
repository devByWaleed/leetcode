class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass

obj = Solution()
print(obj.backspaceCompare("ab#c", "ad#c"))     # True
print(obj.backspaceCompare("ab##", "c#d#"))     # True
print(obj.backspaceCompare("a#c", "b"))         # False