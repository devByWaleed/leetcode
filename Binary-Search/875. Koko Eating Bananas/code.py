from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Minimum bananas can be eaten
        left = 1

        # Maximum bananas
        right = max(piles)
        
        # k -> bananas-per-hour eating speed
        k = 0

        def can_finish(mid):
            total_hours = 0

            for p in piles:
                # Ceiling division to avoid fraction
                total_hours += math.ceil(p / mid)
                # total_hours += (p + mid - 1) // mid

            # If True, then we can go slow
            return total_hours <= h
        

        while left <= right:
            mid = left + (right - left) // 2
            
            # Calculate total hours directly inside the loop
            if can_finish(mid):
                # Best speed
                k = mid

                # Speed works, try slow as given
                right = mid - 1
            else:
                # Too slow, go faster
                left = mid + 1
        
        return k


obj = Solution()
print(obj.minEatingSpeed([3, 6, 7, 11], 8))              # 4
print(obj.minEatingSpeed([30, 11, 23, 4, 20], 5))        # 30
print(obj.minEatingSpeed([30, 11, 23, 4, 20], 6))        # 23

# T.C: O(N * LOG max(piles))
# S.C: O(1)