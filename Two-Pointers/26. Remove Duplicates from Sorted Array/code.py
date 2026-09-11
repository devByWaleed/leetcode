from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Pointer to keep track of next position for unique number
        k = 1

        # Looping from 2nd element as 1st one is unique
        for i in range(1, len(nums)):

            # Condition for arranging non-duplicates
            if nums[i] != nums[i-1]:

                # Re-Assigning the non-duplicate to keep order
                nums[k] = nums[i]

                # Increment counter for next element placing
                k += 1

        return k    # Also works as counter for unique elements
    

obj = Solution()
print(obj.removeDuplicates([1, 1, 2]))                          # 2
print(obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))     # 5

# T.C: O(N)
# S.C: O(1)