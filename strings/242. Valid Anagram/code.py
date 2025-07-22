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