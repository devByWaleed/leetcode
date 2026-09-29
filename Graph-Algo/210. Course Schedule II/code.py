from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Number of prerequisites for each course
        in_degree = [0] * numCourses
        # Save neighbors
        adj_list = {i: [] for i in range(numCourses)}

        result = []

        for a, b in prerequisites:
            # RULE: must take course bi first if you want to take course ai.
            adj_list[b].append(a)
            # Add pre-requisites
            in_degree[a] += 1

        # Adding courses to queue which are ready to taken
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # No. of courses taken
        processed = 0

        while queue:
            # Increment the TAKEN course
            course = queue.popleft()
            result.append(course)

            # Lookup on neighbors
            for neighbor in adj_list[course]:
                # prerequisites requirement finish
                in_degree[neighbor] -= 1

                # If no prerequisite, then neighbor is ready to take
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check that completed all courses
        return result if len(result) == numCourses else []
    

obj = Solution()
print(obj.findOrder(2, [[1,0]]))                            # -> [0,1]
print(obj.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))          # -> [0,2,1,3] or any valid order
print(obj.findOrder(1, []))                                 # -> [0]

# T.C: O(V + E)
# S.C: O(V + E)