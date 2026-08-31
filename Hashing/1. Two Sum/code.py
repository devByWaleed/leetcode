from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define HashMap to store difference for constant lookup
        hash_map = {}

        # Loop through the array
        for i in range(len(nums)):
            # Calculate difference = target - nums[i]
            '''
            For looking a number with current one to satisfy any condition,
            we use difference pattern (a mathematical perspective)
            '''
            difference = target - nums[i]

            # Check if difference in HashMap
            if difference in hash_map:
                # If yes then return both indices i.e., [i, HashMap[difference]]
                return [i, hash_map[difference]]

            # If no, then add {nums[i], i} to HashMap
            else:
                hash_map[nums[i]] = hash_map.get(nums[i], 0) + i

                
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(obj.twoSum([3, 2, 4], 6))        # [1, 2]
print(obj.twoSum([3, 3], 6))           # [0, 1]

# T.C: O(N)     --> Loop through N numbers array
# S.C: O(N)     --> HashMap of N numbers used