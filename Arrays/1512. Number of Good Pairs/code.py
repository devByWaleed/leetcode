from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Count total pairs
        count =  0
        n = len(nums)

        # Frequencies of numbers
        frequency = {}

        # Storing frequencies of numbers
        for i in range(n):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1

        # Using math to find good pairs
        for value in frequency.values():
            count += (value * (value - 1)) // 2


        return count
        

obj = Solution()
print(obj.numIdenticalPairs([1, 2, 3, 1, 1, 3]))       # 4
print(obj.numIdenticalPairs([1, 1, 1, 1]))             # 6
print(obj.numIdenticalPairs([1, 2, 3]))                # 0

# T.C = O(N)
# S.C = O(N)


# Brute force approach
'''
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
'''