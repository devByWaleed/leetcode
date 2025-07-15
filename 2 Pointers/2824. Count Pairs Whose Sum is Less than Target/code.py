from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()     # Sorting for 2-pointers

        n = len(nums)
        left, right = 0, n - 1
        count = 0       # Counts the pairs

        while left < right:
           
           # If condition meets, all values b/w left & right will validate the condition
            if (nums[left] + nums[right]) < target:
                count += right - left
                left += 1

            # If total is not less than, then decrement right pointer
            else:
                right -= 1


        return count


obj = Solution()
print(obj.countPairs([-1, 1, 2, 3, 1], 2))                  # 3
print(obj.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))        # 10

# T.C: O(N log N)
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