from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # gain.insert(0, 0)     # Updating the array with 0 (initial point in description)
        
        # for i in range(1, len(gain)):
              # Updating gains with altitudes
        #     gain[i] = gain[i] + gain[i-1]

        # Returning maximum element
        # return max(gain)


        # net_gain & max_alt to keep track of our values
        net_gain, max_alt = 0, 0

        for i in range(0, len(gain)):

            # Finding net gain
            net_gain = net_gain + gain[i]
            # gain[i] = net_gain        # Optional (it makes the array from gains to net gain i.e., altitudes)

            # Updating the max_alt after finding maximum element
            if max_alt < net_gain:
                max_alt = net_gain
        
        return max_alt
    

obj = Solution()

print(obj.largestAltitude([-5, 1, 5, 0, -7]))               # 1
print(obj.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))       # 0

# T.C = O(N)
# S.C = O(1)