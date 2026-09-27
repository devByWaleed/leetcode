class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []

        # Sorting based on .start
        intervals.sort(key=lambda x: x[0])
        

        for i in range(0, len(intervals)):
            # Overlap
            if result and intervals[i][0] <= result[-1][1]:
                # overlaps last merged interval
                result[-1][1] = max(result[-1][1], intervals[i][1])
            
            # Not overlapped
            else:
                result.append(intervals[i])

        return result


obj = Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(obj.merge([[1,4],[4,5]]))                 # [[1,5]]
print(obj.merge([[4,7],[1,4]]))                 # [[1,7]]

# T.C: O(N LOG N)       --> Sorting + Looping through array
# S.C: O(N)             --> Array used for N intervals