from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

obj = Solution()
print(obj.canFinish(2, [[1,0]]))           # -> True
print(obj.canFinish(2, [[1,0],[0,1]]))     # -> False