from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        result, comb = [], []
        total = 0

        def backtrack(i,total):
            # Base condition
            if total == target:
                result.append(comb.copy())
                return

            # Invalid sum condition
            if i == n or total > target:
                return

            # Add to comb
            comb.append(candidates[i])

            # Cond1: Picked & backtrack
            backtrack(i, total+candidates[i])

            # UNDO
            comb.pop()

            # Cond2: Not Picked
            backtrack(i+1,total)

        # Start backtracking
        backtrack(0,total)

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