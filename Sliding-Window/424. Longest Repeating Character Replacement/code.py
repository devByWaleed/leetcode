class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Store maximum frequency
        max_freq = 0

        # Store final answer
        max_length = 0

        frequencies = {}

        left = 0


        for right in range(len(s)):
            # Add to map
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1

            # Update maximum frequency from MAP
            max_freq = max(max_freq, frequencies[s[right]])

            # Shrinking the window: If replacement needed
            while (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left += 1

            # Update with maximum
            max_length = max(max_length, right - left + 1)

        return max_length


obj = Solution()
print(obj.characterReplacement("ABAB", 2))      # 4
print(obj.characterReplacement("AABABBA", 1))   # 4
print(obj.characterReplacement("AAAA", 2))      # 4
print(obj.characterReplacement("ABAA", 0))      # 2

# T.C: O(N)     --> Looping through string
# S.C: O(1)     --> HashMap used, but it only holds maximum 26 chars i.e., constant overall