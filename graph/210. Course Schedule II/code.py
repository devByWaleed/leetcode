from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass

obj = Solution()
print(obj.findOrder(2, [[1,0]]))                            # -> [0,1]
print(obj.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))          # -> [0,2,1,3] or any valid order
print(obj.findOrder(1, []))                                 # -> [0]