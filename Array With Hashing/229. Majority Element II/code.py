from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
         
        # Frequency target for checking to each element 
        target = n // 3
         
        frequencies = {}
         
        array = []    # To store majority elements 
         
        # Storing frequencies of each element 
        for i in nums:
             
            if i not in frequencies:
                frequencies.update({i: 0})
             
            frequencies[i] += 1
             
         
        for j in frequencies:
             
            # If we find majority element, add it to array
            if frequencies[j] > target:
                array.append(j)
        
        return array
        
        
obj = Solution()
print(obj.majorityElement([3, 2, 3]))       # [3]
print(obj.majorityElement([1]))             # [1]
print(obj.majorityElement([1, 2]))          # [1, 2]

# T.C: O(N)
# S.C: O(N)