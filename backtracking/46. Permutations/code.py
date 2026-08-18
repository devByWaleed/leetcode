from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
                
        # Stores final answer
        result = []
        
        # Stores single pairs
        perm = []

        # Track which element we have worked on
        pick = [False] * n

        def backtrack(perm, nums, pick):
            # Base case to add into result
            if len(perm) == n:
                result.append(perm.copy())
                return

            for i in range(n):
                # If number is not picked yet
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True

                    # Backtrack: Check all possibilities
                    backtrack(perm, nums, pick)

                    # POP ( UNDO )
                    perm.pop()
                    pick[i] = False


        # Call function with initial value
        backtrack(perm, nums, pick)
        return result


obj = Solution()
print(obj.permmute([1, 2, 3]))           # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(obj.permmute([0, 1]))              # [[0,1], [1,0]]
print(obj.permmute([1]))                 # [[1]]

# T.C: O(N * N!)   --> N! permutations for N numbers
# S.C: O(N!)       -->  Recursive call stack used



# Template

'''
result, perm = [], []
pick = [False] * n

backtrack():
    Base condition

    Loop till n
        # Not picked
        Add to perm
        Set pick[i] to True

        backtrack()

        # UNDO
        POP from perm
        Set pick[i] to False

backtrack()
return result
'''