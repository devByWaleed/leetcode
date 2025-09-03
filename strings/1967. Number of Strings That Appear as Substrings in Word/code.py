class Solution:

    def numOfStrings(self, patterns: list[str], word: str) -> int:

        # To count sub-strings
        count = 0

        for i in patterns:
            extract = i
            
            # If current word is sub-string, increment 1
            if extract in word:
                count += 1

        return count


obj = Solution()
print(obj.numOfStrings(["a","abc","bc","d"] , "abc"))    # 3
print(obj.numOfStrings(["a","b","c"], "aaaaabbbbb"))     # 2
print(obj.numOfStrings(["a","a","a"], "ab"))             # 3

# T.C: O(N * M)
# S.C: O(1)