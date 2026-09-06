from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        result = []

        # Assign 1st pointer
        for i in range(0, n-2):
            # Skipping duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Assign 2nd & 3rd pointer
            j = i+1
            k = n-1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # Skipping duplicates
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    # Update pointers
                    j += 1
                    k -= 1

                # Update pointers if pair not found
                elif total_sum < 0:
                    j += 1
                else:
                    k -= 1

        return result

        
obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))    # [[-1, -1, 2],[-1, 0, 1]]
print(obj.threeSum([0, 1, 1]))                # []
print(obj.threeSum([0, 0, 0]))                # [[0, 0, 0]]

# T.C: O(N ^ 2)             --> Nested Loop
# S.C: O(1) / O(LOG N)      --> Depending on sorting