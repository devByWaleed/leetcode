# Using Hash-set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hash_set = set()

        left = 0

        for right in range(len(s)):
            # Shrinking window
            while s[right] in hash_set:
                # Removing from left side and adjusting window
                hash_set.remove(s[left])
                left += 1

            # Add to set
            hash_set.add(s[right])

            # Current window
            window = right - left + 1

            # Update with maximum
            max_length = max(max_length, window)

        return max_length


obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))       # 3
print(obj.lengthOfLongestSubstring("abcabcbb"))     # 3
print(obj.lengthOfLongestSubstring("bbbbb"))        # 1
print(obj.lengthOfLongestSubstring("aab"))          # 2
print(obj.lengthOfLongestSubstring("dvdf"))         # 3

# T.C: O(N)     --> Looping through string
# S.C: O(1)     --> HashSet used, but it never holds more than 1 same character



# Using Ordered-Dictionary
'''
from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0   # save longest sub-string length

        left = 0         # Pointer for expanding window

        frequencies = OrderedDict()    # Track elements for each window

        for right in range(len(s)):

            # If element found in dictionary, remove first element and expand window
            while s[right] in frequencies:
                frequencies.popitem(last=False) 
                left += 1

            # Update the dictionary and then update length of sub-string
            frequencies.update({s[right]: True})

            max_length = max(max_length, right - left + 1)

            
        return max_length


obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))     # 3
print(obj.lengthOfLongestSubstring("bbbbb"))        # 1
print(obj.lengthOfLongestSubstring("pwwkew"))       # 3
print(obj.lengthOfLongestSubstring("aab"))          # 2
print(obj.lengthOfLongestSubstring("dvdf"))         # 3

# T.C: O(N)
# S.C: O(K)
# K = size of the character set (at most number of unique characters in window)
'''