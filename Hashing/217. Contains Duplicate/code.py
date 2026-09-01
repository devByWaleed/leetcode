'''
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

# T.C: O(N)     --> Looping through array
# S.C: O(N)     --> Hash-Set used
'''



class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # SORT to place duplicates side by side
        nums.sort()

        # Track 1st number
        prev = 0

        # Loop to track 2nd number and traverse
        for curr in range(1, len(nums)):
            # Duplicate condition
            if nums[curr] == nums[prev]:
                return True
            else:
                # Move pointer to check other numbers
                prev += 1

        # No duplicate found
        return False


obj = Solution()
print(obj.containsDuplicate([1, 2, 3, 1]))                      # True
print(obj.containsDuplicate([1, 2, 3, 4]))                      # False
print(obj.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))    # True
print(obj.containsDuplicate([2, 14, 18, 22, 22]))               # True

# T.C: O(N LOG N)       --> Looping through array + Sorting
# S.C: O(1)             --> No data structure used