from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        # Store window of size k
        window = set()

        left = 0    # For shrinking window

        for right in range(n):
            # If number found in window, satisfied both conditions
            if nums[right] in window:
                return True
        
            # Update the window with current element
            window.add(nums[right])
        
            # Checks window length with k and remove left-most element
            if right-left == k:
                window.remove(nums[left])
                left += 1
            

        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1, 2, 3, 1], 3))           # True
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))           # True
print(obj.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))     # False

# T.C: O(N)
# S.C: O(K)



# Using Hash-map (track last seen index)
'''
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # Store last seen index of number
        last_index = {}

        for i in range(n):
            # If number found
            if nums[i] in last_index:

                # Check for 2nd condition
                if (abs(i-last_index[nums[i]]) <= k):
                    return True
        
            # Update the last seen index
            last_index.update({nums[i]: i})

        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1, 2, 3, 1], 3))           # True
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))           # True
print(obj.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))     # False

# T.C: O(N)
# S.C: O(N)
'''