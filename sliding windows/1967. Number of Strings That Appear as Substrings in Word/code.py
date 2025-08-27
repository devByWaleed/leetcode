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