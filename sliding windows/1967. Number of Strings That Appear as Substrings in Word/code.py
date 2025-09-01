from collections import Counter

class Solution:

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0

        # Storing frequencies of "word"
        frequencies = {}

        for i in word:

            frequencies[i] = frequencies.get(i, 0) + 1

        # Flag to verify whole word as sub-string
        is_sub = False
        

        for j in patterns:

            # Individual word
            word_counter = dict(Counter(j))

            
            for k in word_counter:

                # If key is not present in frequencies, flag will False(not a sub-string)
                if k not in frequencies:
                    is_sub = False
                
                # If the frequencies of current word is matched, flag will True
                elif word_counter[k] <= frequencies[k]:
                    is_sub = True
                    # continue
                    
            # After loop, whole word is sub-string, increment the counter 
            if is_sub:
                count += 1
                
            
        return count
        

obj = Solution()
print(obj.numOfStrings(["a","abc","bc","d"] , "abc"))    # 3
print(obj.numOfStrings(["a","b","c"], "aaaaabbbbb"))     # 2
print(obj.numOfStrings(["a","a","a"], "ab"))             # 3
print(obj.numOfStrings(["cjevwg"], "jevwg"))             # 0, but 1 is giving

# T.C: O(m + pi)
# S.C: O(u + p_{max})
'''
m = length of word
pi = length of each pattern
p_{max} = maximum length among patterns.
u = unique chars in word
'''



# Brute Force Solution
'''

class Solution:

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        n = len(patterns)
        for i in range(0, n):
            extract = patterns[i]
            
            if extract in word:
                count += 1

        return count

obj = Solution()
print(obj.numOfStrings(["a","abc","bc","d"] , "abc"))    # 3
print(obj.numOfStrings(["a","b","c"], "aaaaabbbbb"))     # 2
print(obj.numOfStrings(["a","a","a"], "ab"))             # 3

# T.C: O(N * M)
# S.C: O(1)
'''