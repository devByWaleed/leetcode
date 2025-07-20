class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):    return False


obj = Solution()
print(obj.isIsomorphic("egg", "add"))       # True
print(obj.isIsomorphic("foo", "bar"))       # False
print(obj.isIsomorphic("paper", "title"))   # True