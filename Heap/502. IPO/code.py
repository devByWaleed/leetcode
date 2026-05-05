from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Using to remain the input same
        c = w
        n = len(profits)

        # MAX_HEAP stores max profit
        max_heap = []
        
        # Pairing capital and profit
        projects = []
        for i in range(n):
            projects.append((capital[i], profits[i]))
        
        # Sort by capital
        projects.sort()

        # Counter to track current project
        counter = 0

        for _ in range(k):
            # Adding profit to heap
            while counter < n and projects[counter][0] <= c:
                heapq.heappush(max_heap, -projects[counter][1])
                counter += 1
            
            # If empty we can't start new project
            if not max_heap:
                break

            # Pop the profit and add it to final capital
            c += -heapq.heappop(max_heap)

        return c


obj = Solution()
print(obj.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))     # 4
print(obj.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))     # 6

# T.C: O(N LOG N + K LOG N)
# S.C: O(N LOG N + K LOG N) -> O(N)