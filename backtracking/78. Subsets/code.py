from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # Store all subsets
        result = []

        # Current subset
        sub_set = []

        def backtrack(i):
            # If we get all combinations
            if i == n:
                result.append(sub_set.copy())
                return
            
            # Don't pick nums[i]
            backtrack(i+1)

            # Pick nums[i]
            sub_set.append(nums[i])
            backtrack(i+1)
            sub_set.pop()

        # Call bactrack function for 1st element
        backtrack(0)

        return result


obj = Solution()
print(obj.subsets([1, 2, 3]))           # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
print(obj.subsets([0]))                 # [[], [0]]

# T.C: O(N * 2^N)
# S.C: O(N)