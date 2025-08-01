class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):     return ""

        required = {}
        window = {}

        have, need = 0, len(required)

        left, minLen = 0, float('inf')

        minL, minR = 0, 0


        for i in range(len(t)):

            required[t[i]] = required.get(t[i], 0) + 1


        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in required and window[char] == required[char]:
                have += 1

            while have == need:

                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    minL = left
                    minR = right
            

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in required and window[leftChar] < required[leftChar]:
                    have -= 1

                left += 1

        return "" if minLen == float('inf') else s[minL: minR+1]
        # return "" if minLen == 0 else s[minL: minLen]



obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))        # BANC
print(obj.minWindow("a", "a"))                      # a
print(obj.minWindow("a", "aa"))                     # 