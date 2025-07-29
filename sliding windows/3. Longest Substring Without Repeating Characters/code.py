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




# Failed For Test-Cases
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0   # save longest sub-string length
        max_count = 0   # max frequency for single char in current window

        frequencies = {}    # Track frequecies for each window

        for left in range(len(s)):

            if s[left] in frequencies:
                max_count -= 1
                if max_length < max_count:    max_length = max_count

            else:
                frequencies[s[left]] = frequencies.get(s[left], 0) + 1
                max_count += 1
                if max_length < max_count:    max_length = max_count
            
        
        return max_length
        # return frequencies, max_count, max_length


obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))     # 3
print(obj.lengthOfLongestSubstring("bbbbb"))        # 1
print(obj.lengthOfLongestSubstring("pwwkew"))       # 3
print(obj.lengthOfLongestSubstring("aab"))          # 2
print(obj.lengthOfLongestSubstring("dvdf"))         # 3

# T.C: O(N)
# S.C: O(1)
'''