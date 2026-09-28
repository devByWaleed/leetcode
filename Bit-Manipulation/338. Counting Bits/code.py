from typing import List

# DP Approach
class Solution:
    def countBits(self, n: int) -> List[int]:       
        # DP Array for final answer
        ans = [0] * (n+1)

        for i in range(1, n+1):
            # add bit count + signal for even/odd
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


obj = Solution()
print(obj.countBits(2))      # [0, 1, 1]
print(obj.countBits(5))      # [0, 1, 1, 2, 1, 2]

# T.C: O(N)     --> Looping + constant bit-operation through N times
# S.C: O(N)     --> DP array of size N used


# Brian Kernighan’s Algorithm (Number-by-Number)
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        def checkBits(num):
            weight = 0

            # Count bits for single number by discarding 1 (LSB)
            while num != 0:
                num = num & (num - 1)
                weight += 1

            return weight

        # Loop including n to count and add to ans
        for i in range(0, n+1):
            val = checkBits(i)
            ans.append(val)

        return ans

    
obj = Solution()
print(obj.countBits(2))      # [0, 1, 1]
print(obj.countBits(5))      # [0, 1, 1, 2, 1, 2]

# T.C: O(N LOG N)     --> Right Shifting operation on N numbers
# S.C: O(N)         --> Array used to store N numbers
'''