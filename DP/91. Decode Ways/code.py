class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: leading zero
        if s[0] == "0":
            return 0
        
        # dp array of size s+1
        n = len(s)
        dp = [0] * (n + 1)

        # Set default values
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            single = s[i-1]
            double = s[i-2:i]

            # Updation for single character
            if single != "0":
                dp[i] += dp[i-1]

            if 10 <= int(double) <= 26:
                dp[i] += dp[i-2]
        
        # Last index holds possible ways
        return dp[n]


obj = Solution()
print(obj.numDecodings("12"))   # 2
print(obj.numDecodings("226"))  # 3
print(obj.numDecodings("06"))   # 0

# T.C: O(N)     --> Looping through N length string
# S.C: O(N)     --> DP array of size N used

'''
- Edge case: if s[0] == "0, simply return 0
- Create a dp array of size n+1
- Set Default Values: set dp[0] = 1 for single character
- Set Default Values: set dp[1] = 1 for leading zero
- Loop from range(2, n):
    - if s[i-1] != "0", add dp[i-1] into dp[i] for only single letter way
    - if int(s[i-2:i]) is in range of (10, 26), add dp[i-2] into dp[i] for only double letters way
- At the end, return dp[n]
'''