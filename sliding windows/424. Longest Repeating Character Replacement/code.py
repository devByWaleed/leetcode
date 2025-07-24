class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_subString = 0   # save longest sub-string length
        current_len = 1    # for starting with 1 index, current should be 1

        s = list(s)     # for replacement

        for i in range(1, len(s)):
            
            # If current and previous is same
            if s[i] == s[i-1]:  
                current_len += 1
                if max_subString < current_len:     max_subString = current_len
                continue

            # Codition for replacement
            elif s[i] != s[i-1] and k != 0:
                s[i] = s[i-1]
                current_len += 1
                k -= 1
                max_subString = max(max_subString, current_len)

            # If not same but we have no chance to replace
            elif s[i] != s[i-1] and k == 0:
                max_subString = max(max_subString, current_len)
                break       # when k = 0, will no replace so loop should be break

        return max_subString


obj = Solution()
print(obj.characterReplacement("AABA", 0))      # 1 but 2
print(obj.characterReplacement("ABAB", 2))      # 4
print(obj.characterReplacement("AABABBA", 1))   # 4
print(obj.characterReplacement("AAAA", 2))      # 4


