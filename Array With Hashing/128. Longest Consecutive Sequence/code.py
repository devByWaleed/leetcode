from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Edge case for empty array
        if len(nums) == 0:
            return 0
        
        # Edge case for 1 element array
        if len(nums) == 1:
            return 1
        
        # Convert the input list to a set for O(1) lookups and to remove duplicates.
        hash_set = set(nums)

        # Store longest consecutive sequence.
        longest = 0

        for num in hash_set:

            # If num is start of sequence or not
            if num - 1 not in hash_set:
                streak = 1      # streak to keep track of longest sequence

                # Incrementing the loop number & streak while the num is in set
                while num + 1 in hash_set:
                    streak += 1
                    num += 1

                # Updating the longest sequence by longest streak
                longest = max(longest, streak)

        return longest



obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))                   # 4
print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))           # 9
print(obj.longestConsecutive([1, 0, 1, 2]))                             # 3
print(obj.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))      # 7
print(obj.longestConsecutive([1, 2, 0, 1]))                             # 3
print(obj.longestConsecutive([0]))                                      # 1
print(obj.longestConsecutive([0, 0]))                                   # 1
print(obj.longestConsecutive([]))                                       # 0

# T.C: O(N)
# S.C: O(N)




###### or
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Edge case for empty array
        if len(nums) == 0:
            return 0
        
        # Edge case for 1 element array
        if len(nums) == 1:
            return 1
        
        # Convert the input list to a set for O(1) lookups and to remove duplicates.
        hash_set = set(nums)

        # Store longest consecutive sequence.
        longest = 0

        for num in hash_set:

            # Check if 'num' is the start of a sequence (i.e., num-1 is not in the set).
            if num - 1 not in hash_set:
                current_num = num      # Start of the current sequence.
                current_streak = 1     # Initialize the streak length.

                # Continue to check for the next consecutive number in the set.
                while current_num + 1 in hash_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak if the current one is longer.
                longest = max(longest, current_streak)


        # Return longest consecutive sequence.
        return longest


obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))                   # 4
print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))           # 9
print(obj.longestConsecutive([1, 0, 1, 2]))                             # 3
print(obj.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))      # 7
print(obj.longestConsecutive([1, 2, 0, 1]))                             # 3
print(obj.longestConsecutive([0]))                                      # 1
print(obj.longestConsecutive([0, 0]))                                   # 1
print(obj.longestConsecutive([]))                                       # 0

# T.C: O(N)
# S.C: O(N)
'''