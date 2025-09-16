from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        char_freq = {}

        # count the length of word formed by chars
        counter = 0

        # Counting frequencies of each letter in chars
        for i in range(len(chars)):

            if chars[i] not in char_freq:
                char_freq.update({chars[i]: 0})

            char_freq[chars[i]] += 1
        
        # Nested loop to check for each letter
        for j in words:

            # Counting frequencies of each word
            word_freq = Counter(j)

            can_form = True
            for k in word_freq:

                # Checking for presence based on frequencies
                if not k in char_freq or not char_freq[k] >= word_freq[k]:
                    can_form = False    # To skip whole word if letter not in chars
                    break
            
            # If word can be formed, add its length
            if can_form:
                counter += len(j)
            
        return counter


obj = Solution()
print(obj.countCharacters(["cat", "bt", "hat", "tree"], "atach"))               # 6
print(obj.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))    # 10

# T.C: O(N + M)
# S.C: O(N + M)