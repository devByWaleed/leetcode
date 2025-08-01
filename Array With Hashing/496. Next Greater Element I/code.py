from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        len1, len2 = len(nums1), len(nums2)
        
        # ans array of nums1 array length
        ans = [0] * len1

        # Pointer to keep track of next greater element
        pointer = 0

        for i in range(len1):

            for j in range(len2):

                # If both arrays elements equal, we go for next greater element search
                if nums1[i] == nums2[j]:

                    # To keep checking next element within the length
                    if j + 1 < len2:
                        pointer = j + 1     # Index of next element

                        # If next element is greater than current, assign it to ans array
                        if nums2[pointer] > nums2[j]:
                            ans[i] = nums2[pointer]
                        
                        # If not the next element, then check for remaining
                        elif nums2[pointer] <= nums2[j]:
                            
                            while nums2[pointer] <= nums2[j]:
                            # while nums2[pointer] <= nums2[j] and pointer < len2:
                                pointer += 1

                            ans[i] = nums2[pointer]
                        
                        # If no greatest element, add -1
                        else:
                            ans[i] = -1
                        
                    
                    # Condition for both elements at arrays end-point
                    else:
                        ans[i] = -1

        return ans


obj = Solution()
print(obj.nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))          # [7, 7, 7, 7, 7]
print(obj.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))                         # [-1, 3, -1]
print(obj.nextGreaterElement([2, 4], [1, 2, 3, 4]))                            # [3, -1]