from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Initializing 2 pointers
        slow = nums[0]
        fast = nums[0]
            
        # Checking for cycle
        while True:
                
            slow = nums[slow]
            fast = nums[nums[fast]]
                
            if slow == fast:
                break
                
        # Resetting 1 pointer
        slow = nums[0]
            
            
        while slow != fast:
                
            slow = nums[slow]
            fast = nums[fast]
            
        return fast    # Duplicate number
    

obj = Solution()
print(obj.findDuplicate([1, 3, 4, 2, 2]))   # 2
print(obj.findDuplicate([3, 1, 3, 4, 2]))   # 3
print(obj.findDuplicate([3, 3, 3, 3, 3]))   # 3

# T.C: O(N) 
# S.C: O(1)