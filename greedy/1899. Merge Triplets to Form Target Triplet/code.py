from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pass


obj = Solution()
print(obj.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))      # True
print(obj.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))      # False
print(obj.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))      # True