from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Couting common numbers in both array
        answer1, answer2 = 0, 0

        hash_map1 = {}
        hash_map2 = {}


        # Adding values to hash_map for O(1) search
        for i in range(len(nums1)):

            if nums1[i] not in hash_map1:
                hash_map1.update({nums1[i]: 0})
            
            hash_map1[nums1[i]] += 1
        

        # Adding values to hash_map for O(1) search
        for j in range(len(nums2)):

            if nums2[j] not in hash_map2:
                hash_map2.update({nums2[j]: 0})
            
            hash_map2[nums2[j]] += 1


        # Checking for numbers in hashmap to increase counter
        for i in range(len(nums1)):

            if nums1[i] in hash_map2:
                answer1 += 1
        
        
        # Checking for numbers in hashmap to increase counter
        for j in range(len(nums2)):

            if nums2[j] in hash_map1:
                answer2 += 1


        return [answer1, answer2]


obj = Solution()
print(obj.findIntersectionValues([2, 3, 2], [1, 2]))                     # [2, 1]
print(obj.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))   # [3, 4]
print(obj.findIntersectionValues([3, 4, 2, 3], [1, 5]))                  # [0, 0]

# T.C: O(N + M)
# S.C: O(N + M)



# Brute Force (Checking in array)
'''
from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Couting common numbers in both array
        answer1, answer2 = 0, 0

        # Counting for nums1 array
        for i in nums1:

            if i in nums2:
                answer1 += 1
        
        # Counting for nums2 array
        for j in nums2:

            if j in nums1:
                answer2 += 1


        return [answer1, answer2]


obj = Solution()
print(obj.findIntersectionValues([2, 3, 2], [1, 2]))                     # [2, 1]
print(obj.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))   # [3, 4]
print(obj.findIntersectionValues([3, 4, 2, 3], [1, 5]))                  # [0, 0]

# T.C: O(N * M)
# S.C: O(1)
'''