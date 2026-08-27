# Knuth-Morris-Pratt (KMP) Algorithm
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # Stores longest prefix suffix length for each element of string
        lps = [0] * n

        # Track previous
        prev_lps = 0
        i = 1

        while i < n:
            # If char matched
            if s[i] == s[prev_lps]:
                # Increment length
                prev_lps += 1
                # Update longest length
                lps[i] = prev_lps
                # Move to next element
                i += 1
            # If not matched
            else:
                # Not negative
                if prev_lps > 0:
                    prev_lps = lps[prev_lps - 1]
                # If 0, then update array with 0
                elif prev_lps == 0:
                    lps[i] = 0
                    # Move to next element
                    i += 1

        # Longest prefix suffix length of s
        L = lps[n-1]

        # Condition 1: string is not empty
        cond1 = L > 0

        # Condition 2: Even length
        cond2 = n % (n-L)

        # MOD return 0 (Falsy), so use not
        return cond1 and not cond2


obj = Solution()
print(obj.repeatedSubstringPattern("abab"))             # True
print(obj.repeatedSubstringPattern("aba"))              # False
print(obj.repeatedSubstringPattern("abcabcabcabc"))     # True

# T.C: O(N)     --> Loop through N elements
# S.C: O(N)     --> lps array of size N






# Brute Force
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # Doubling the original string
        double = s + s

        # Remove 1st and last character
        double = double[1: len(double)-1]

        # find() method to check index. If -1, it is not a sub-string pattern
        value = double.find(s) 
        return value != -1


obj = Solution()
print(obj.repeatedSubstringPattern("abab"))             # True
print(obj.repeatedSubstringPattern("aba"))              # False
print(obj.repeatedSubstringPattern("abcabcabcabc"))     # True

# T.C: O(N)
# S.C: O(N)
'''