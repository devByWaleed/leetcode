from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            
            # Backtrack: Include this number
            comb.append(candidates[i])
            backtrack(i, total + candidates[i])

            # POP ( UNDO )
            comb.pop()

            # Backtrack: Skip this number
            backtrack(i+1, total)


        # Call function with initial value
        backtrack(0, total)
        return result


obj = Solution()
print(obj.combinationSum([2, 3, 6, 7], 7))              # [[2,2,3],[7]]
print(obj.combinationSum([2, 3, 5], 8))                 # [[2,2,2,2],[2,3,3],[3,5]]
print(obj.combinationSum([2], 1))                       # []

# T.C: O(K * 2^T), O(N ^ (T/M))  --> where T is the target, M is the minimum value in candidates, and N is the length of candidates.
# S.C: O(N)                      -->  Recursive call stack used


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

    # UNDO
    POP from comb
    
    backtrack(i+1,total)

backtrack(0,total)
return result
'''