class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for _ in range(len(s)):

            # Rotating 1st char to the end
            s = s[1:] + s[0]

            # Checking for desired result
            if s == goal:   return True

        # If not found, return False
        return False



obj = Solution()
print(obj.rotateString("abcde", "cdeab"))       # True
print(obj.rotateString("abcde", "abced"))       # False

# T.C: O(N ^ 2)
# S.C: O(1)



# ******** or
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # Concatenation of s
        s = s + s

        # Checking for existense
        return goal in s


obj = Solution()
print(obj.rotateString("abcde", "cdeab"))       # True
print(obj.rotateString("abcde", "abced"))       # False

# T.C: O(N)
# S.C: O(1)
'''