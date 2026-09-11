from typing import List

class Solution:
    # def reverseString(self, s: List[str]) -> None:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        if n == 1:  return s    # Edge case

        # Pointers at start & end
        left = 0
        right = n - 1

        # 2 Pointers condition
        while left < right:

            # Swapping
            s[left], s[right] = s[right], s[left]

            # Updating the pointers
            left += 1
            right -= 1

        return s


obj = Solution()
print(obj.reverseString(["h", "e", "l", "l", "o"]))             # ["o", "l", "l", "e", "h"]
print(obj.reverseString(["H", "a", "n", "n", "a", "h"]))        # ["h", "a", "n", "n", "a", "H"]

# T.C: O(N)
# S.C: O(1)