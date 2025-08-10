from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Store n / 2 in a varaible
        target = n // 2

        frequencies = {}

        # Adding to hash_map by number:frequency
        for i in range(n):

            if nums[i] not in frequencies:
                frequencies.update({nums[i]: 0})
            
            frequencies[nums[i]] += 1

        # Looping through hash_map
        for key in frequencies:

            # If frequency found, return that number
            if frequencies[key] > target:
                return key


obj = Solution()
print(obj.majorityElement([3, 2, 3]))                 # 3
print(obj.majorityElement([2, 2, 1, 1, 1, 2, 2]))     # 2

# T.C: O(N)
# S.C: O(N)