from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # Store the frequencies of each number
        frequencies = {}

        # Loop over array to get the frequency of each number
        for i in range(len(arr)):

            if arr[i] not in frequencies:
                frequencies.update({arr[i]: 0})
            
            frequencies[arr[i]] += 1

        # Checking the length of frequecies and set of frequencies for uniqueness
        return len(set(frequencies.values())) == len(frequencies.values())


obj = Solution()
print(obj.uniqueOccurrences([1, 2, 2, 1, 1, 3]))                    # True
print(obj.uniqueOccurrences([1, 2]))                                # False
print(obj.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))    # True
print(obj.uniqueOccurrences([-130,21,-154,159,-44,-126,165,68,-126,-126,-126,128,-94,165,-30,-44,-39,-94,21,-130,68,68,128,-130,-39,181,68,68,68,139,139,-39,21,21,-39,68,128,131,-126,-154,-30,165,21,159,181,-39,-126,131,-94,-44,131,128,21,-44,128,-94,183,-94,131,139,-44,128,21,181,-44,131,128,131,21,68,181,-44,-126,-130,131,-190,131,181,165,-94,165,165,-30,-154,68,-39,-44,165,-39,-126,68,68,-130,68,-94,181,-44,131,21,183,-44,21,-39,-130,-39,131,21,165,165,-126,165,-44,-94,68,68,-94,-126,-126,-30,181,165,68,-44,-39,-94,-126,-126,-30,68,181,-44,-94,-126,-44,-94,-30,131,165,-190,-130,-94,-94,181,128,181,181,181,139,-130,-94,-130,-130,139,-130,-90,-154,181,165,-30,-154,165,-190,159,165,139,-126,-44,131,-44,-190,-126,-130,-94,128,-154,68,-130,-130,68,21,-44,-30,-126,-126,131,159,-190,-126,181,139]))    # False

# T.C: O(N)  --> O(N) + O(K)
# S.C: O(N)  --> O(K) + O(K) + O(K)