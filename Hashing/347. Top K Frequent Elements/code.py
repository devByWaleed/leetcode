# HashMap + Min-Heap

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Store frequencies
        frequencies = {}

        # MinHeap for Top K, result for final answer
        min_heap, result = [], []

        # 1: Store frequencies
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1

        # 2: Update MinHeap with Top K Frequent elements
        for num, frequency in frequencies.items():
            heapq.heappush(min_heap, (frequency, num))

            # If size exceeded, remove smallest one
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 3: Add the actual number to result
        for pair in min_heap:
            result.append(pair[1])

        return result


obj = Solution()
print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))       # [1, 2]
print(obj.topKFrequent([1], 1))                      # [1]
print(obj.topKFrequent([3, 0, 1, 0], 1))             # [0]

# T.C: O(N log K)   --> Main MinHeap of K elements for N total numbers
# S.C: O(N)         --> MinHeap + result array used



# HashMap + Sorting
"""
from typing import List

'''
- This problem divides into 3 parts. Counting-frequencies -> Sorting by frequency -> Adding k elements
- We need to sort hash_map in descending order to get higher frequencies at top.
- Then loop k times to get that element
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Hashmap to store frequencies of each number
        count = {}

        # Array to save object (to be sorted)
        # frequencies = []

        # Array will save top k elements
        result = []


        for i in nums:
            # get method to initialize value to 0
            count[i] = count.get(i, 0) + 1

        
        # for key, value in count.items():

        #     frequencies.append({value: key})
            # frequencies.append({key: value})

        # Sorting the array of objects in reverse order
        frequencies = sorted(count.items(), key=lambda x: x[1], reverse=True)
        

        for i in range(k):
            # Appending the top k element (not the frequencies)
            result.append(frequencies[i][0])


        return result
        

obj = Solution()
print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))       # [1, 2]
print(obj.topKFrequent([1], 1))                      # [1]
print(obj.topKFrequent([3, 0, 1, 0], 1))             # [0]

# T.C: O(N log N)
# S.C: O(N)
"""