from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # Store all palindrome
        result = []

        # Currnt palindrome
        pal = []

        def backtrack(i):
            # If we get all palindromes
            if i >= n:
                result.append(pal.copy())
                return
            
            # Checking for all possible palindrome
            for j in range(i, n):
                if self.is_pal(s, i, j):
                    # Add palindrome
                    pal.append(s[i: j+1])

                    # Call for next element
                    backtrack(j+1)

                    # UNDO the step
                    pal.pop()


        # Call bactrack function for 1st element
        backtrack(0)
        return result
    

    # Private function to check palindrome
    def is_pal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


obj = Solution()

print(obj.partition("aab"))     # [["a","a","b"], ["aa","b"]]
print(obj.partition("a"))       # [["a"]]

# T.C: O(N * 2^N)
# S.C: O(N)