class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # Hash set for cheking for duplicate elements
        hash_set = set()
        
        for value in nums:

            # If value is in set, return True. else add it to set
            if value in hash_set: 
                return True 
            else:
                hash_set.add(value)

        return False

obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))  # True
print(obj.containsDuplicate([3, 3]))        # True

# T.C: O(N)
# S.C: O(N)