class Solution:
    def hammingWeight(self, n: int) -> int:
       # Total set bits
        count = 0

        num = n

        while num > 0:
            # Checking 1 bit
            num = num & (num-1)

            # Increment count
            count += 1
        
        return count


obj = Solution()
print(obj.hammingWeight(11))            # 3
print(obj.hammingWeight(128))           # 1
print(obj.hammingWeight(2147483645))    # 30

# T.C: O(K)     --> Number of set bits
# S.C: O(1)     --> No data structure used