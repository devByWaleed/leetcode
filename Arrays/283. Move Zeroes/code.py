# Approach 3: Single Pass

from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Pointer for keep track of non-zero number's index
        slow = 0

        # Pointer for iteration
        for fast in range(n):

            # If zero found, increment fast by 1
            if nums[fast] == 0:
                fast += 1
            
            else:
                # Tackling un-necessary swapping
                if slow != fast:

                    # Swap the zero with non-zero number
                    nums[slow], nums[fast] = nums[fast], nums[slow]

                # Incrementing slow for next element 
                slow += 1

        return nums

        
obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]
print(obj.moveZeroes([1, 0]))               # [1, 0]

# T.C:  O(N)
# S.C:  O(1)


# -------------------------------------------------------------------


# Approach 2: 2 Passes
'''
from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Pointer for updating non-zero numbers
        write_index = 0

        
        for read_index in range(n):
            # If non-zero found, update & increment write_index by 1
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1

                
        # Updating all remaining indices to 0
        for i in range(write_index, n):
            nums[i] = 0
            

        return nums

        
obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]
print(obj.moveZeroes([1, 0]))               # [1, 0]

# T.C:  O(N)
# S.C:  O(1)
'''


# -------------------------------------------------------------------


# Approach 1 (Brute Force): Creating a new list
'''
from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ans = [0] * n

        # Pointer for iteration
        i = 0

        # Pointer for ans array (non-zero)
        start = 0

        # Pointer for 0
        end = n - 1

        while i < n:

            if nums[i] == 0:

                # Assigning 0 to the end of array
                ans[end] = nums[i]

                # Decrementing for right place
                end -= 1
            else:

                # ans[i] for starting of ans array
                ans[start] = nums[i]

                # Incrementing for right place
                start += 1
            
            i += 1

        return ans

        
obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]

# T.C: O(N)
# S.C: O(N)
'''