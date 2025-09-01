from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count =  0
        n = len(nums)

        for i in range(n):

            for j in range(n):

                if (nums[i] == nums[j]) and (i < j):

                    count += 1
        
        return count
        

obj = Solution()
print(obj.numIdenticalPairs([1, 2, 3, 1, 1, 3]))       # 4
print(obj.numIdenticalPairs([1, 1, 1, 1]))             # 6
print(obj.numIdenticalPairs([1, 2, 3]))                # 0

# T.C = O(N ^ 2)
# S.C = O(1)