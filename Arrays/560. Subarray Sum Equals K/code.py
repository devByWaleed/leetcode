from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Map to store prefix sums and their frequencies.
        frequency = {0: 1}

        # Final answer: Total subarrays
        subarray_count = 0

        # Running cumulative prefix sum
        current_sum = 0

        for i in range(n):
            # Add current window sum
            current_sum += nums[i]

            # If we found (current_sum - k), we found the subarray
            if current_sum - k in frequency:
                subarray_count += 1

            # Update the frequency of the current prefix sum
            frequency[current_sum] = frequency.get(current_sum, 0) + 1

        return subarray_count
    

obj = Solution()
print(obj.subarraySum([1, 1, 1], 2))  # Output: 2
print(obj.subarraySum([1, 2, 3], 3))  # Output: 2

# T.C: O(N)     --> Loop on N numbers
# S.C: O(N)     --> N numbers in HashMap