from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Return -1 if impossible
        if sum(gas) < sum(cost):
            return -1

        curr = start = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            # Current value
            curr += g - c

            # Negative, not enough gas
            if curr < 0:
                # Next station is impossible
                start = i + 1
                curr = 0

        return start
        

obj = Solution()
print(obj.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))      # 3
print(obj.canCompleteCircuit([2, 3, 4], [3, 4, 3]))      # -1

# T.C: O(N)
# S.C: O(1)



# Brute force
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        curr = start = 0

        for i, (g, c) in enumerate(zip(gas+gas, cost+cost)):
            # If seen the current station
            if i == start + n:
                return start
            
            # Current value
            curr += g - c

            # Negative, not enough gas
            if curr < 0:
                # Next station is impossible
                start = i + 1
                curr = 0
        
        # Return -1 if impossible
        return -1


obj = Solution()
print(obj.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))      # 3
print(obj.canCompleteCircuit([2, 3, 4], [3, 4, 3]))      # -1
'''
# T.C: O(N)
# S.C: O(N)