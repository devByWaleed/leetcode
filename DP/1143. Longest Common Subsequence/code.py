class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # Track LCS
        lcs = 0

        # DP initialization with list comprehension
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp = []
        # 2D DP array
        for _ in range(m + 1):
            dp.append([0] * (n + 1))


        for i in range(m):
            for j in range(n):
                # If letter matched
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # If not matched, take max of top & left neighbor
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                # Update length with maximum one
                lcs = max(lcs, dp[i][j])

        # for i in range(len(dp)):
        #     lcs = max(lcs, max(dp[i]))

        return lcs


obj = Solution()


# Test Case 1
text1 = "abcde"
text2 = "ace"
print(obj.longestCommonSubsequence(text1, text2))    # 3


# Test Case 2
text1 = "abc"
text2 = "abc"
print(obj.longestCommonSubsequence(text1, text2))    # 3


# Test Case 3
text1 = "abc"
text2 = "def"
print(obj.longestCommonSubsequence(text1, text2))    # 0

# T.C: O(M * N)     --> M = len(text1), N = len(text2), filling the dp table
# S.C: O(M * N)     --> dp table of size (M+1) x (N+1)