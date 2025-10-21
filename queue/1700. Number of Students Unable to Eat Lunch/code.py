from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)
        take = 0
        # infinite = 0

        while students:

            # If student take sandwich
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                take += 1
            
            # Student will go to end of line
            else:
                current = students.pop(0)
                students.append(current)

        unable = n - take
        return unable

obj = Solution()
print(obj.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))    # 3
print(obj.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))                # 0