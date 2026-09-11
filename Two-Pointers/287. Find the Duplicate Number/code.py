from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Initializing fast and slow pointers
        slow = nums[0]
        fast = nums[0]

        # Pointer movement must be: P_{next} = P_{current}

        # 1st, we find intersection of 2 numbers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Reset 1 pointer to start and move 1 time
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]


        return slow     # Duplicate number will be on other pointer
    

obj = Solution()
print(obj.findDuplicate([1, 3, 4, 2, 2]))   # 2
print(obj.findDuplicate([3, 1, 3, 4, 2]))   # 3
print(obj.findDuplicate([3, 3, 3, 3, 3]))   # 3

# T.C: O(N) 
# S.C: O(1)