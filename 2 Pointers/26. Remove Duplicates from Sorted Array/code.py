from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Pointer to keep track of duplicates
        k = 1

        for i in range(1, len(nums)):

            # Condition for arranging non-duplicates
            if nums[i] != nums[i-1]:

                # Re-Assigning the non-duplicate 
                nums[k] = nums[i]

                # Counter to count uniques elements
                k += 1

        return k
    
obj = Solution()
print(obj.removeDuplicates([1, 1, 2]))                          # 2
print(obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))     # 5

# T.C: O(N)
# S.C: O(1)