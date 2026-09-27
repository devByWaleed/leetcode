class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)

        # Sorting based on .end
        intervals.sort(key=lambda x: x[1])

        # Track smallest
        last_end = -float("inf")

        count = 0        

        for i in range(0, n):
            current = intervals[i]
            
            # If tracker is smaller, update it
            if last_end <= current[0]:
                last_end = current[1]
            
            # Else add counter to skip it
            else:
                count += 1
            
        return count


obj = Solution()
print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))     # 1
print(obj.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))           # 2
print(obj.eraseOverlapIntervals([[1,2],[2,3]]))                 # 0

# T.C: O(N LOG N)       --> Sorting + Looping through array
# S.C: O(1)             --> No data structure used