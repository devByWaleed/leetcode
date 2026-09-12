class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # Count all substrings
        total_palindrome = 0

        def expand_towards_center(i, j):
            # Return total count
            count = 0

            # Index Inbound & palindrome checking
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1

                # Expanding towards center
                i -= 1
                j += 1

            return count

        
        for i in range(n):
            # Odd length center
            total_palindrome += expand_towards_center(i, i)

            # Even length center
            total_palindrome += expand_towards_center(i, i+1)

        # Final count
        return total_palindrome


obj = Solution()
print(obj.countSubstrings("abc"))       # 3
print(obj.countSubstrings("aaa"))       # 6

# T.C: O(N ^ 2)     --> Nested looping
# S.C: O(1)         --> No data structure used