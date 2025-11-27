from typing import List

'''
- Add edge cases to tackle smallest constraints
- According to description, nothing to do with redundant number. Hence  create a hash_set for constant lookup on unique numbers. This is sorted in ascending order.
- If previous number is present, we know streak will not be increase. If we add it, it will be redundant. 
- If not present, we can start our streak and go on to the numbers which are present in set, inside while loop. If next number is not present, we come to know that it's next number will also not in set as it is consecutive sequence.
- After while loop, just update streak with longest sequence by checking maximum number. After loop, return it.
'''

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