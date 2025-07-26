class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0       # Counts good sub-string
        
        # Loop range for not getting out of bound error
        for i in range(0, len(s) - 2):

            # Aquiring the sub-string
            char1 = s[i]
            char2 = s[i + 1]
            char3 = s[i + 2]

            # Checking for good sub-string

            # No need for third condition as math law implemented
            # if (char1 != char2) and (char2 != char3):
            if (char1 != char2) and (char2 != char3) and (char3 != char1):
                count += 1

        return count


obj = Solution()
print(obj.countGoodSubstrings("xyzzaz"))        # 1
print(obj.countGoodSubstrings("aababcabc"))     # 4