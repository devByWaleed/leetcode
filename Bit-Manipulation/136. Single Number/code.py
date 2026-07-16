from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Track that single number
        track = 0

        for i in range(len(nums)):
            # It will overwrite the track if same number occurs again.
            track = nums[i] ^ track
        
        return track


obj = Solution()
print(obj.singleNumber([2,2,1]))      # 1
print(obj.singleNumber([4,1,2,1,2]))      # 4
print(obj.singleNumber([1]))      # 1

# T.C: O(N)
# S.C: O(1)