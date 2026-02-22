from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        # Store all combinations
        result = []

        # Current combination
        path = []

        # To group duplicates together
        candidates.sort()

        # Calculating sum
        total = 0

        def backtrack(i, path, total):
            # If we find sum, add the combination
            if total == target:
                result.append(path.copy())
                return

            # Invalid sum
            if i == n or target < total:
                return
            
            # Pick candidates[i]
            path.append(candidates[i])

            # 1 occurence
            backtrack(i+1, path, total+candidates[i])

            # To skip duplicate combinations
            index = i + 1
            while index < n and candidates[index] == candidates[i]:
                index += 1

            # UNDO the step
            path.pop()

            # Call for next element
            backtrack(index, path, total)
            # backtrack(i+1, path, total)

        # Call bactrack function for 1st element
        backtrack(0, path, total)

        return result


obj = Solution()
print(obj.combinationSum2([2, 5, 2, 1, 2], 5))              # [[1,2,2], [5]]
print(obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))       # [[1,1,6], [1,2,5], [1,7], [2,6]]

# T.C: O(2^N)
# S.C: O(N)