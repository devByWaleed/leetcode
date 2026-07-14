# Bit-by-Bit Shift
class Solution:
    def hammingWeight(self, n: int) -> int:
        # store number of 1's bit
        weight = 0

        for pos in range(n.bit_length()):
            # shifting bit
            shifted = n >> pos

            # if result is 1, increase weight
            if shifted & 1:
                weight += 1

        return weight


obj = Solution()
print(obj.hammingWeight(11))            # 3
print(obj.hammingWeight(128))           # 1
print(obj.hammingWeight(2147483645))    # 30

# T.C: O(LOG N)
# S.C: O(1)


# Brian Kernighan’s Algorithm
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
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


obj = Solution()
print(obj.hammingWeight(11))            # 3
print(obj.hammingWeight(128))           # 1
print(obj.hammingWeight(2147483645))    # 30

# T.C: O(1)
# S.C: O(1)
'''