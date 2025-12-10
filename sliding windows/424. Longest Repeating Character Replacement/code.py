class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Hash-set for record of repeated characters
        hash_map = {}

        # For shrinking window
        left = 0

        # Calculate maximum length
        max_len = 0

        max_count = 0   # window max frequency

        # Iterating through string
        for right in range(0, len(s)):

            # Adding character to hash-map
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            # Checking for maximum frequesncy of char in current window
            max_count = max(max_count, hash_map[s[right]])

            # Remove left-most characters from window
            while ((right - left) + 1) - max_count > k:
                hash_map[s[left]] -= 1
                left += 1

            
            # Updating maximum size
            max_len = max(max_len, ((right - left) + 1))

        return max_len


obj = Solution()
print(obj.characterReplacement("ABAB", 2))      # 4
print(obj.characterReplacement("AABABBA", 1))   # 4
print(obj.characterReplacement("AAAA", 2))      # 4
print(obj.characterReplacement("ABAA", 0))      # 2

# T.C: O(N)
# S.C: O(1)