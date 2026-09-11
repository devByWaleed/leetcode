class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Store total stones, are also jewels
        total_jewels = 0
        
        for i in jewels:

            # count() method to check frequency 
            frequency = stones.count(i)
            total_jewels += frequency

        return total_jewels

obj = Solution()
print(obj.numJewelsInStones("aA", "aAAbbbb"))   # 3
print(obj.numJewelsInStones("z", "ZZ"))         # 0

# T.C: O(M * N)
# S.C: O(1)