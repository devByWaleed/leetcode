from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # Creating a static array of length 2n
        ans = [0] * (2 * n)

        for i in range(0, n):

            # Assigning values as per description
            ans[i], ans[i + n] = nums[i], nums[i]

        return ans


obj = Solution()
print(obj.getConcatenation([1, 2, 1]))      # [1, 2, 1, 1, 2, 1]
print(obj.getConcatenation([1, 3, 2, 1]))   # [1, 3, 2, 1, 1, 3, 2, 1]

# T.C = O(N)
# S.C = O(N)