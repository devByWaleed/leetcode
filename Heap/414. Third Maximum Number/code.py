from typing import List
import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Edge case, only 1 number
        if len(nums) == 1:
            return nums[0]
        
        # Define Heap
        min_heap = []

        # Handle duplicates
        hash_set = set(nums)
        
        for i in hash_set:
            # Add number to heap
            heapq.heappush(min_heap, i)

            # If length exceeds, remove smallest number
            if len(min_heap) > 3:
                heapq.heappop(min_heap)
            

        # If only 2 numbers, return maximum number
        if len(min_heap) == 2:
            return min_heap[-1]

        # Return 3rd maximum number
        return min_heap[0]


obj = Solution()
print(obj.thirdMax([3, 2, 1]))                       # 1
print(obj.thirdMax([1, 2]))                          # 2
print(obj.thirdMax([2, 2, 3, 1]))                    # 1
print(obj.thirdMax([1, 2, 2, 5, 3, 5]))              # 2

# T.C: O(N)
# S.C: O(N)