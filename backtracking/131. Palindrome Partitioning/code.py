from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
                        
        # Stores final answer
        result = []
        
        # Stores single palindrome
        pal = []

        def backtrack(i):
            # Base case to add into result
            if i >= n:
                result.append(pal.copy())
                return

            for j in range(i, n):
                # Checking for palindrome
                if self.is_pal(s, i, j):
                    # Add string with help of indexing
                    pal.append(s[i: j+1])

                    # Backtrack: New element
                    backtrack(j+1)

                    # POP ( UNDO )
                    pal.pop()


        # Call function with initial value
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

# T.C: O(N * 2^N)  --> N-1 potential cut for N length string
# S.C: O(N)        --> Recursive call stack used



# Template

'''
result, pal = [], []

backtrack(i):
    Base condition

    Loop till (i,n)
        # Not picked
        Add to pal

        backtrack(j+1)

        # UNDO
        POP from pal

backtrack(0)
return result
'''