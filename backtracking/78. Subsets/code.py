from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        # Stores final answer
        result = []
        
        # Stores single pairs
        sub_sets = []
        
        def backtrack(i):
            # Base case to add into result
            if i == n:
                result.append(sub_sets.copy())
                return
            
            # Backtrack: Don't pick nums[i]
            backtrack(i+1)

            # Backtrack: Pick nums[i]
            sub_sets.append(nums[i])
            backtrack(i+1)
            
            # POP ( UNDO )
            sub_sets.pop()
        
        # Call function with initial value
        backtrack(0)
        return result


obj = Solution()
print(obj.sub_sets([1, 2, 3]))           # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
print(obj.sub_sets([0]))                 # [[], [0]]

# T.C: O(N * 2^N) --> 2^N sub_sets for N numbers
# S.C: O(N)       --> Recursive call stack used





# Template

'''
result, sub_sets = [], []

backtrack(i):
    Base condition

    # Backtrack
    backtrack(i+1)

    # Picked picked
    Add to sub_sets
    backtrack(i+1)

    # UNDO
    POP from sub_sets

backtrack(0)
return result
'''



# Answer in reversed form
'''
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # Store all sub_sets
        result = []

        # Current subset
        per = []

        def backtrack(i):
            # If we get all combinations
            if i == n:
                result.append(per.copy())
                return
            
            # Don't pick nums[i]
            # backtrack(i+1)

            # Pick nums[i]
            per.append(nums[i])
            backtrack(i+1)
            per.pop()
            backtrack(i+1)

        # Call bactrack function for 1st element
        backtrack(0)

        return result


obj = Solution()
print(obj.permute([1, 2, 3]))           # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(obj.permute([0, 1]))              # [[0,1], [1,0]]
print(obj.permute([1]))                 # [[1]]
'''