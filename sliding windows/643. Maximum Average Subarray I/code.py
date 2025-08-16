from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)

        # Calculating sum of first k elements
        window_sum = sum(nums[:k])

        # max_sum to keep track maximum value
        max_sum = window_sum

        # Loop through remaining window
        for i in range(k, n):

            # At each iteration, we add current value and subtract previous one
            window_sum += nums[i] - nums[i - k]

            # Updating maximum sum
            max_sum = max(max_sum, window_sum)

        # Calculating average of maximum sum (i,e., maximum average)
        average = max_sum / k
        
        return average
    

obj = Solution()
print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))                # 12.75000
print(obj.findMaxAverage([5], 1))                                   # 5.00000
print(obj.findMaxAverage([3, 3, 4, 3, 0], 3))                       # 3.33333
print(obj.findMaxAverage([6, 8, 6, 8, 0, 4, 1, 2, 9, 9], 2))        # 9.00000
print(obj.findMaxAverage([4, 0, 4, 3, 3], 5))                       # 2.80000
print(obj.findMaxAverage(
    [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891], 93))                       # -594.58065

# T.C: O(N)
# S.C: O(1)


# Inefficient for large inputs
'''
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)

        # We declared -ve infinity as we may get negative max average
        max_avg = -float('inf')

        # Edge case
        if n == 1 and k == 1:
            return nums[0]

        # for i in range(0, n-2):       # this loop range causes wrong window ranges
        
        # Loop range n-k+1(for inclusive n-k) to get elements in window size range, not error or missing last numbers
        for i in range(0, n-k+1):

            # Numbers according to window size
            window_element = nums[i: i+k]

            # Calculating average
            average = sum(window_element) / k

            # Updating the maximum average
            max_avg = max(max_avg, average)

        return max_avg
    

obj = Solution()
print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))                # 12.75000
print(obj.findMaxAverage([5], 1))                                   # 5.00000
print(obj.findMaxAverage([3, 3, 4, 3, 0], 3))                       # 3.33333
print(obj.findMaxAverage([6, 8, 6, 8, 0, 4, 1, 2, 9, 9], 2))        # 9.00000
print(obj.findMaxAverage([4, 0, 4, 3, 3], 5))                       # 2.80000
print(obj.findMaxAverage(
    [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891], 93))                       # -594.58065

# T.C: O(N . K)
# S.C: O(K)  maybe
'''