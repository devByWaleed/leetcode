class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if len(s) < len(t):     return ""

        # Store frequencies of t
        required = {}

        # Store frequencies of current window
        window = {}

        for i in range(len(t)):
            required[t[i]] = required.get(t[i], 0) + 1


        # To track current & required window length
        have, need = 0, len(required.keys())
        
        # Track kength of minimum sub-string
        minLen = float('inf')
        
        # Two pointers for tracking sub-string
        minL, minR = 0, 0

        left = 0  # Fir window shrinking

        for right in range(len(s)):

            char = s[right]

            # Adding char at current window
            window[char] = window.get(char, 0) + 1

            # Checking for same
            if char in required and window[char] == required[char]:
                have += 1


            while have == need:
                # When we find window, Assign minimum legth and set pointers
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    minL = left
                    minR = right
            
                # Removing left-most char
                leftChar = s[left]
                window[leftChar] -= 1
                left += 1

                # If removing this character breaks a required frequency, mark the window as invalid
                if leftChar in required and window[leftChar] < required[leftChar]:
                    have -= 1


        # Return the string
        return "" if minLen == float('inf') else s[minL: minR+1]
        # return "" if minLen == 0 else s[minL: minR+1]


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))        # BANC
print(obj.minWindow("a", "a"))                      # a
print(obj.minWindow("a", "aa"))                     # ""

# T.C: O(M + N)
# S.C: O(K)