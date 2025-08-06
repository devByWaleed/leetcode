from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pass

obj = Solution()
print(obj.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))    # ["Mary", "Emma", "John"]
print(obj.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))     # ["Bob", "Alice", "Bob"]