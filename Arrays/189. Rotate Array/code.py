from typing import List

class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """

        size = len(nums)

        # Manage edge case where k > size of array
        if k > size:
            k = k % size
        
        for i in range(0, k):
            rot = nums.pop()
            nums.insert(0, rot)

        return nums


obj = Solution()
print(obj.rotate([1, 2, 3, 4, 5, 6, 7], 3))     # [5, 6, 7, 1, 2, 3, 4]
print(obj.rotate([-1, -100, 3, 99], 2))         # [3, 99, -1, -100]

# T.C: O(K * N)
# S.C: O(1)