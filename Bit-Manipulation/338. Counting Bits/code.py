# DP Approach
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:       
        # DP Array for final answer
        ans = [0] * n+1

        for i in range(1, n+1):
            # add bit count + signal for even/odd
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


obj = Solution()
print(obj.countBits(2))      # [0, 1, 1]
print(obj.countBits(5))      # [0, 1, 1, 2, 1, 2]

# T.C: O(N)
# S.C: O(N)




# Brian Kernighan’s Algorithm (Number-by-Number)
'''
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        def oneBits(n):
            # Weight of current number
            weight = 0
            
            # Saving a copy
            num = n

            while num != 0:
                # Perform AND operation
                num = num & (num-1)

                # Increase weight
                weight += 1

            return weight
        
        # Array for final answer
        ans = []

        for i in range(n+1):
            set_bits = oneBits(i)
            ans.append(set_bits)

        return ans        


obj = Solution()
print(obj.countBits(2))      # [0, 1, 1]
print(obj.countBits(5))      # [0, 1, 1, 2, 1, 2]

# T.C: O(LOG N)
# S.C: O(N)
'''