class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        
        # Track adding 
        added = False

        for i in range(len(intervals)):
            # Before newInterval
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            
            # After newInterval
            elif intervals[i][0] > newInterval[1]:
                if not added:
                    result.append(newInterval)
                    added = True
                result.append(intervals[i])
            
            # Overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # Add overlapped if don't added yet
        if not added:
            result.append(newInterval)

        return result


obj = Solution()
print(obj.insert([[1,3],[6,9]], [2,5]))                         # [[1,5],[6,9]]
print(obj.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))    # [[1,2],[3,10],[12,16]]

# T.C: O(N)     --> Looping through array
# S.C: O(N)     --> Array used for N intervals