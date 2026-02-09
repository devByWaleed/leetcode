from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular = 0
        # square = 1
        # students = queue
        # sandwiches = stack
        take = 0            # Track of student able to eat
        infinite = 0        # To check for infinite loop
        
        queue = deque(students)     # Using deque for efficient removal
        stack = deque(sandwiches)
        
        while queue and stack:
          
          # If student take sandwich
          if queue[0] == stack[0]:
            queue.popleft()
            stack.popleft()
            take += 1
            infinite = 0    # Re-setting for smooth record
            
          # Student will go to end of line
          else:
            front = queue.popleft()
            queue.append(front)
            infinite += 1
            
            # For same result again and again
            if infinite == len(queue):  break
          
        # Calculating the students who are unable to eat
        return len(students) - take


obj = Solution()
print(obj.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))                # 0
print(obj.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))    # 3

# T.C: O(N)
# S.C: O(N)