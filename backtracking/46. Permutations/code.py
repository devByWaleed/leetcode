from typing import List

class Solution:
    def permmute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # Store all permmutations
        result = []

        # Current permmutation
        perm = []

        # To track which element we have worked on
        pick = [False] * n

        def backtrack(perm, nums, pick):
            # If we get valid permmutation
            if len(perm) == n:
                result.append(perm.copy())
                return

            # Picking permutation
            for i in range(n):

                # If number is not picked
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True

                    # Explore all possibilities
                    backtrack(perm, nums, pick)

                    # Undo the state
                    perm.pop()
                    pick[i] = False


        # Call bactrack function
        backtrack(perm, nums, pick)

        return result


obj = Solution()
print(obj.permmute([1, 2, 3]))           # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(obj.permmute([0, 1]))              # [[0,1], [1,0]]
print(obj.permmute([1]))                 # [[1]]

# T.C: O(N * N!)
# S.C: O(N!)