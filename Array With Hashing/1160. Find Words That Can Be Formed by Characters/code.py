from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        '''char_freq = {}

        word_freq = {}

        for i in range(len(chars)):

            if chars[i] not in char_freq:
                char_freq.update({chars[i]: 0})

            char_freq[chars[i]] += 1
        
        
        for j in range(len(chars)):

            if chars[j] not in word_freq:
                word_freq.update({chars[j]: 0})

            word_freq[chars[j]] += 1
        
        return char_freq'''


obj = Solution()
print(obj.countCharacters(["cat", "bt", "hat", "tree"], "atach"))               # 6
print(obj.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))    # 10