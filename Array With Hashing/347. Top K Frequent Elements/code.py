from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Hashmap to store frequencies of each number
        count = {}

        # Array to save object (to be sorted)
        frequencies = []

        # Array will save top k elements
        result = []


        for i in nums:
            # get method to initialize value to 0
            count[i] = count.get(i, 0) + 1

        
        for key, value in count.items():

            frequencies.append({value: key})
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