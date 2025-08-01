from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # Creating answer array of 2 size
        answer = [[], []]
        
        # Converting both arrays to set for tackling distinct elements
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Iterating over 1st set
        for i in set1:
            
            if i not in set2:
                # Adding the element to 1st array of answer
                answer[0].append(i)
                
        # Iterating over 2nd set        
        for j in set2:
            
            if j not in set1:
                # Adding the element to 2nd array of answer
                answer[1].append(j)

        
        return answer
        
        
obj = Solution()
print(obj.findDifference([1, 2, 3], [2, 4, 6]))         # [[1, 3],[4, 6]]
print(obj.findDifference([1, 1, 2, 3], [1, 1, 2, 2]))   # [[3],[]]

# T.C: O(N + M)
# S.C: O(N + M)