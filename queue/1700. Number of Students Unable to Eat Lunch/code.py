from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)
        queue = deque(students)     # Using deque for efficient removal
        stack = deque(sandwiches)
        take = 0            # Track of student able to eat
        infinite = 0        # To check for infinite loop

        while queue:

            # If student take sandwich
            if queue[0] == stack[0]:
                queue.popleft()
                stack.popleft()
                take += 1
                infinite = 0    # Re-setting for smooth record
            
            # Student will go to end of line
            else:
                current = queue.popleft()
                queue.append(current)
                infinite += 1

                # Check for infinite loop
                if infinite == len(queue):  break

        # Calculating the students who are unable to eat
        unable = n - take
        return unable


obj = Solution()
print(obj.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))                # 0
print(obj.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))    # 3

# T.C: O(N)
# S.C: O(N)