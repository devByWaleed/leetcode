class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Cases
        if len(t) > len(s) :   return ""

        # Store frequencies of t'chars
        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Store substrings
        window = {}

        # have track the occurences of s in t
        # need is the total frequencies of t
        have, need = 0, len(count_t.keys())

        # Store final answer
        min_len = float("inf")

        # Pointers to track sub-string from s
        min_l, min_r = 0, 0

        # for window shrinking
        left = 0

        # For window expanding
        for right in range(len(s)):
            char = s[right]

            # Update window
            window[char] = window.get(char, 0) + 1

            # Update on finding t's char
            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    # Update minimum length & pointers for s
                    min_len = right - left + 1
                    min_l = left
                    min_r = right

                # Shrinking window
                left_char = s[left]
                window[left_char] -= 1
                left += 1

                # Decrement count for validation of window
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
            

        # +1 will add last index element
        return "" if min_len == float("inf") else s[min_l: min_r+1]


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))        # BANC
print(obj.minWindow("a", "a"))                      # a
print(obj.minWindow("a", "aa"))                     # ""

# T.C: O(M + N)     --> Loop through string "t" + "s"
# S.C: O(K)         --> HashMap used to store K size window