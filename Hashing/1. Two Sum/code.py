from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        # Using hash map for constant time operation
        hash_map = {}

        for i in range(n):

            # calculating difference
            difference = target - nums[i]
            
            # If not found in hash map, it includes number as key & index as value
            if difference not in hash_map:
                hash_map[nums[i]] = i

            # If found, return that index of hashmap and current loop's value
            else:
                return [hash_map[difference], i]

        # Edge case for not founding anything
        return []


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(obj.twoSum([3, 2, 4], 6))        # [1, 2]
print(obj.twoSum([3, 3], 6))           # [0, 1]

# T.C: O(N)
# S.C: O(N)