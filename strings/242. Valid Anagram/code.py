class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: Different length
        if len(s) != len(t):
            return False

        hash_map = {}

        # Storing frequencies
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        for c in t:
            # If not in HashMap, then no anagram
            if c not in hash_map:
                return False
            else:
                # If frequency is 1, delete
                if hash_map[c] == 1:
                    del hash_map[c]

                # Else decrement frequency
                else:
                    hash_map[c] -= 1

        # t is anagram of s
        return True

        
obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))      # True
print(obj.isAnagram("rat", "car"))              # False

# T.C: O(N)     —> Looping through string
# S.C: O(1)     —> HashMap data structure used, but will be empty if t is anagram. Plus all lowercase (26) english chars is far low than 128 possible combinations in ASCII.

# Follow-up: For Unicode, approach will be same. But the space complexity increases from O(1) to O(min(N, Σ)). Where Σ is unicode-set length and N is length of s