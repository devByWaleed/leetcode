from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        
        # Empty hashset of size k
        window = set()

        for i in range(n):

            # Checking for duplicates (1st condition)
            if nums[i] in window:
                return True
            
            # add if not present
            window.add(nums[i])

            # Keeping the window of size k by removing old element, enforce 2nd condition
            if i >= k:
                window.discard(nums[i-k])

        # If after iterating all over array, return False
        return False


obj = Solution()
print(obj.containsNearbyDuplicate([1, 2, 3, 1], 3))           # True
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))           # True
print(obj.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))     # False

# T.C: O(N)
# S.C: O(K)



# Nested loop (brute force thinking)
'''from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):

            for j in range(len(nums)):

                if i == j:  continue

                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        
        return False

obj = Solution()
print(obj.containsNearbyDuplicate([1, 2, 3, 1], 3))           # True
print(obj.containsNearbyDuplicate([1, 0, 1, 1], 1))           # True
print(obj.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))     # False'''