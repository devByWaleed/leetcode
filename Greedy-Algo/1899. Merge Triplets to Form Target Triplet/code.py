from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Final triplet after checking all
        [max_a, max_b, max_c] = [0, 0, 0]

        for arr in triplets:
            # Checking for values
            c1 = arr[0] <= target[0]
            c2 = arr[1] <= target[1]
            c3 = arr[2] <= target[2]

            # If all values are smaller, then this can become target
            if c1 and c2 and c3:
                max_a = max(max_a, arr[0])
                max_b = max(max_b, arr[1])
                max_c = max(max_c, arr[2])

        # Comparison gives answer
        return [max_a, max_b, max_c] == target


obj = Solution()
print(obj.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))      # True
print(obj.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))      # False
print(obj.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))      # True

# T.C: O(N)
# S.C: O(1)