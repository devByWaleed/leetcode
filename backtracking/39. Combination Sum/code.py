from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        # Store all combinations
        result = []

        # Current combination
        path = []

        # Calculating sum
        total = 0

        def backtrack(i, path, total):
            # # If we find sum, add the combination
            if total == target:
                result.append(path.copy())
                return

            # Invalid sum
            if i == n or target < total:
                return
            
            # Pick candidates[i]
            path.append(candidates[i])

            # Many occurences
            backtrack(i, path, total+candidates[i])

            # UNDO the step
            path.pop()

            # Call for next element
            backtrack(i+1, path, total)

        # Call bactrack function for 1st element
        backtrack(0, path, total)

        return result


obj = Solution()
print(obj.combinationSum([2, 3, 6, 7], 7))              # [[2,2,3],[7]]
print(obj.combinationSum([2, 3, 5], 8))                 # [[2,2,2,2],[2,3,3],[3,5]]
print(obj.combinationSum([2], 1))                       # []

# T.C: O(K * 2^T), O(N ^ (T/M))
# S.C: O(N)