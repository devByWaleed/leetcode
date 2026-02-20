from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # Store all subsets
        result = []

        # Current subset
        sub_set = []

        # To group duplicates together
        nums.sort()

        def backtrack(i):
            # If we reaches end, add  the subset
            if i == n:
                result.append(sub_set.copy())
                return

            # Pick nums[i]
            sub_set.append(nums[i])
            backtrack(i+1)
            
            # To skip duplicates
            index = i + 1
            while index < n and nums[index] == nums[i]:
                index += 1

            # UNDO the step
            sub_set.pop()

            # For next non-duplicate number
            backtrack(index)

        # Call bactrack function for 1st element
        backtrack(0)

        return result


obj = Solution()
print(obj.subsetsWithDup([1, 2, 2]))           # [[], [1], [1,2], [1,2,2], [2], [2,2]]
print(obj.subsetsWithDup([0]))                 # [[], [0]]

# T.C: O(N * 2^N)
# S.C: O(N)