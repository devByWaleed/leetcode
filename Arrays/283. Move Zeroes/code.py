# Approach 1: Single Pass
from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Index where non-zero number placed
        slow = 0

        for fast in range(n):
            # If zero, ignore
            if nums[fast] == 0:
                continue
            else:
                # Prevents un-necessary swapping
                if slow != fast:
                    # 1 liner swap
                    '''
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    '''
                    # Swapping using temp
                    temp = nums[fast]
                    nums[fast] = nums[slow]
                    nums[slow] = temp

                # Increment position
                slow += 1

        return nums


obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]
print(obj.moveZeroes([1, 0]))               # [1, 0]

# T.C:  O(N)    --> Loop through N numbers
# S.C:  O(1)    --> No extra space use


# -------------------------------------------------------------------


# Approach 2: 2 Passes
'''
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Index where non-zero numbers placed
        write = 0

        # For remaining indices
        read = 0

        for i in range(n):
            # If number is non-zero, assign it to start of array
            if nums[i] != 0:
                nums[write] = nums[i]
                # Help to assign numbers sequentially
                write += 1

            read = write

        # Assign 0 to remaining indices
        for j in range(read, n):
            nums[j] = 0

        return nums


obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]
print(obj.moveZeroes([1, 0]))               # [1, 0]

# T.C:  O(N)    --> Loop through N numbers
# S.C:  O(1)    --> No extra space use
'''