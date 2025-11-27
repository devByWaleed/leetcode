'''
- Store frequencies of s, so that we can compare from t
- Edge case, if length is not same, it is not anagram
- If char is not same, then it will not be anagram
- If length is 1, simply delete it.
- If length > 1, decrement it. Hence an empty hash_map will show that it is anagram
- All lowercase (26) english chars is far low thna 128 possible combinations in ASCII. Hence it's space is constant

- 2 hash_maps for both strings and then comparison is also a solution, but not as recommended.

- For unicode, strategy will be same but it's space will become linear to N.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Edge case if length of both strings are not same
        if len(t) != len(s):
            return False 

        # Stores frequencies of string s
        hash_map = {}

        # Getting frequencies
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        # Checking for frequencies
        for char in t:

            # If not matched, it is not anagram
            if char not in hash_map:
                return False
            
            # If freq == 1, simply delete it
            elif hash_map[char] == 1: del hash_map[char]
            
            # If freq > 1, decrement it
            else:
                hash_map[char] -= 1
        

        return not hash_map     # True if empty, False otherwise


obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))      # True
print(obj.isAnagram("rat", "car"))              # False

# T.C: O(N), M == N
# S.C: O(1)


# Other solution
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Edge case if length of both strings are not same
        if len(t) != len(s):
            return False 

        # Hash maps to store letter's frequencies of both strings
        count_t = {}
        count_s = {}
        
        for i in range(len(t)):
            # Updating hashmaps with letter's length
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            count_s[s[i]] = count_s.get(s[i], 0) + 1

        # Comparison to check whether it is anagram or not
        return count_t == count_s


obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))      # True
print(obj.isAnagram("rat", "car"))              # False

# T.C: O(N)
# S.C: O(N)
'''