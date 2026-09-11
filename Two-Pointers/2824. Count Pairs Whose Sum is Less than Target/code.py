from typing import List

'''
Approach:-

Use 2 pointers. One point to 0 index and other points to last index

While looping, check that sum of both numbers are less than to target. If yes, then all the numbers appears b/w those indices give same result. After that, increment left pointer.

If sum is greater than target, then move right pointer

Using difference technique will get all numbers sum which meets condition, reduces time complexity from N^2 to N. This is known as Monotonic Two-Pointer Principle

'''


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count = 0   # count total pairs
        
        nums.sort()     # To use 2 pointers

        n = len(nums)

        left, right = 0, n - 1

        while left < right:
            # If we find indices, then add all numbers in range
            if nums[left] + nums[right] < target:
                count += (right-left)
                left += 1   # Increment left pointer
            else:
                right -= 1  # Decrement right pointer

        return count


obj = Solution()
print(obj.countPairs([-1, 1, 2, 3, 1], 2))                  # 3
print(obj.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))        # 10

# T.C: O(N LOG N)
# S.C: O(1)



# Nested Loop (Brute Force)
'''
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        count = 0


        for i in range(0, n):
            for j in range(i+1, n):

                total = nums[i] + nums[j]

                if total < target:
                    count += 1
            

        return count


obj = Solution()
print(obj.countPairs([-1, 1, 2, 3, 1], 2))                  # 3
print(obj.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))        # 10

# T.C: O(N ^ 2)
# S.C: O(1)
'''