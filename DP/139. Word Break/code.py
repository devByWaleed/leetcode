from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # Creating set for O(1) lookup
        words = set(wordDict)

        # DP array with False as initial state
        dp = [False] * (n+1)

        # Base case: empty string
        dp[0] = True

        # Looking for sub-strings for each s[i]
        for i in range(1, n + 1):
            for j in range(i):
                # If sub-string amtches the word
                if dp[j] and s[j:i] in words:
                    # Set True
                    dp[i] = True
                    # Breaking for sub-string
                    break

        # Store final answer
        return dp[n]


obj = Solution()


# Test Case 1
s = "leetcode"
wordDict = ["leet", "code"]
print(obj.wordBreak(s, wordDict))    # True


# Test Case 2
s = "applepenapple"
wordDict = ["apple", "pen"]
print(obj.wordBreak(s, wordDict))    # True


# Test Case 3
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(obj.wordBreak(s, wordDict))    # False

# T.C: O(N^2 * k)     --> N = len(s), nested loop plus substring slicing/lookup
# S.C: O(N + M)   --> dp array of size N, wordSet of total dict characters M