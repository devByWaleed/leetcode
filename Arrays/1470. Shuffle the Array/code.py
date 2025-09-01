from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        size = len(nums)

        # Creating a new array of 2n length
        ans = [0] * size

        # Initializing 2 Pointers
        x, y = 0, 0

        # Run the loop until x (starting pointer) reaches 2nd last element
        while x < size - 1:
            ans[x] = nums[y]
            ans[x+1] = nums[n+y]
            
            # Incrementing by 2 to point towards right index of ans
            x += 2

            # Incrementing by 1 to point next element of nums
            y += 1

        return ans

obj = Solution()
print(obj.shuffle([2,5,1,3,4,7], 3))        # [2, 3, 5, 4, 1, 7]
print(obj.shuffle([1,2,3,4,4,3,2,1], 4))    # [1, 4, 2, 3, 3, 2, 4, 1]
print(obj.shuffle([1,1,2,2], 2))            # [1, 2, 1, 2]

# T.C = O(size)
# S.C = O(size)