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
        start = 0

        # Pointer for ans array (non-zero)
        i = 0

        # Pointer for 0
        end = n - 1

        while start < n:

            if nums[start] == 0:

                # Assigning 0 to the end of array
                ans[end] = nums[start]

                # Decrementing for right place
                end -= 1
            else:

                # ans[i] for starting of ans array
                ans[i] = nums[start]

                # Incrementing for right place
                i += 1
            
            start += 1

        return ans

        
obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]

# T.C: O(start)
# S.C: O(1)


# Not a proper solution
'''
from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Pointer for iteration
        left = 0

        # Pointer for keep track of non-zero numbers
        right = 0

        # Condition for iterating through array 
        while left < n:

            # If zero, only incremented by 1
            if nums[left] == 0:
                left += 1
            
            else:

                # Swap the zero with non-zero number
                nums[left], nums[right] = nums[right], nums[left]

                # Incrementing both pointers 
                left += 1
                right += 1

        return nums

        
obj = Solution()
print(obj.moveZeroes([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
print(obj.moveZeroes([0]))                  # [0]

# T.C:     O(N)
# S.C:     O(1)
'''