from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # SORT the array
        candidates.sort()

        n = len(candidates)
                
        # Stores final answer
        result = []
        
        # Stores single pairs
        comb = []

        # Track current total
        total = 0

        def backtrack(i, total):
            # Base case to add into result
            if total == target:
                result.append(comb.copy())
                return

            # Invalid Sum conditions
            if i == n or total > target:
                return

            # Backtrack: Pick candidates[i] then removing from comb if matched
            comb.append(candidates[i])
            backtrack(i+1, total+candidates[i])

            # New index to check duplicates
            index = i + 1
            while index < n and candidates[index] == candidates[i]:
                # Skip the duplicate
                index += 1
            
            # POP ( UNDO )
            comb.pop()

            # Backtrack: New index to skip the duplicates
            backtrack(index, total)
        

        # Call function with initial value
        backtrack(0, total)
        return result


obj = Solution()
print(obj.combinationSum2([2, 5, 2, 1, 2], 5))              # [[1,2,2], [5]]
print(obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))       # [[1,1,6], [1,2,5], [1,7], [2,6]]

# T.C: O(2^N)  --> N candidates can chosen or skip
# S.C: O(N)    -->  Recursive call stack used


# Template

'''
result, comb = [], []
total = 0

backtrack(i,total):
    Base condition

    Invalid sum condition

    # Not picked
    Add to comb

    backtrack(i,total+candidate[i])

    # New index to check duplicates
    index = i + 1
    while index < n and candidates[index] == candidates[i]:
        # Skip the duplicate
        index += 1

    # UNDO
    POP from comb
    
    backtrack(index, total)

backtrack(0,total)
return result
'''