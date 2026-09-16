from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # SORT the array
        nums.sort()

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

            # Backtrack: Pick nums[i] then removing from sub_sets if matched
            sub_sets.append(nums[i])
            backtrack(i+1)

            # New index to check duplicates
            index = i + 1
            while index < n and nums[index] == nums[i]:
                # Skip the duplicate
                index += 1
            
            # POP ( UNDO )
            sub_sets.pop()

            # Backtrack: New index to skip the duplicates
            backtrack(index)
        
        # Call function with initial value
        backtrack(0)
        return result


obj = Solution()
print(obj.subsetsWithDup([1, 2, 2]))           # [[], [1], [1,2], [1,2,2], [2], [2,2]]
print(obj.subsetsWithDup([0]))                 # [[], [0]]

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

    index = i + 1
    while index is in range & both index'values matches
        increment i with 1

    # UNDO
    POP from sub_sets

    # Backtrack
    backtrack(index)

backtrack(0)
return result
'''