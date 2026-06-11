from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass

obj = Solution()
print(obj.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))  
# -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(obj.pacificAtlantic([[1]]))  # -> [[0,0]]