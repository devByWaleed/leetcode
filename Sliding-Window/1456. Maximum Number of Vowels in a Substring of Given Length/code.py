class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # Hashset for vowel checking
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Edge case
        if len(s) == 1 and s in vowels:
            return 1

        # Track maximum vowels in substring
        max_vowels = 0

        # Vowels in current window
        sub_vowel = 0

        window = s[:k]

        # Counting vowels in first k elements
        for i in window:
            
            if i in vowels:
                sub_vowel += 1

        # Updating after 1st k elements
        max_vowels = sub_vowel

        # Looping through remaining window
        for j in range(k, len(s)):

            # If current and previous is vowel, continue
            if s[j-k] in vowels and s[j] in vowels:
                # max_vowels = max(max_vowels, sub_vowel)
                continue
            
            # If current is not vowel and previous is vowel, decrement count and update
            elif s[j-k] in vowels and s[j] not in vowels:
                sub_vowel -= 1
                max_vowels = max(max_vowels, sub_vowel)
            
            # If current is vowel and previous is not vowel, increment count and update
            elif s[j-k] not in vowels and s[j] in vowels:
                sub_vowel += 1
                max_vowels = max(max_vowels, sub_vowel)
            
        return max_vowels


obj = Solution()
print(obj.maxVowels("abciiidef", 3))                     # 3
print(obj.maxVowels("aeiou", 2))                         # 2
print(obj.maxVowels("leetcode", 3))                      # 2
print(obj.maxVowels("a", 1))                             # 1
print(obj.maxVowels("qempburycnhrvvccr", 13))            # 2

# T.C: O(N)
# S.C: O(1)



# Counting on each window from scratch (not optimal)
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # Hashset for vowel checking
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Edge case
        if len(s) == 1 and s in vowels:
            return 1

        # Track maximum vowels in substring
        max_vowels = 0

        # Vowels in current window
        sub_vowel = 0

        # Loop range for all sub-strings
        for i in range(0, len(s)-2):

            sub_string = s[i:k+i]

            # Nested loop for checking of vowels
            for j in sub_string:

                if j in vowels:
                    sub_vowel += 1
                else:
                    sub_vowel += 0
            
            # Updating maximum vowels and resetting current window
            max_vowels = max(max_vowels, sub_vowel)
            sub_vowel = 0

        return max_vowels


obj = Solution()
print(obj.maxVowels("abciiidef", 3))    # 3
print(obj.maxVowels("aeiou", 2))        # 2
print(obj.maxVowels("leetcode", 3))     # 2
print(obj.maxVowels("a", 1))            # 1
'''