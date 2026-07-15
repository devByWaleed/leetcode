class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_bit = 0
        num = n

        for _ in range(32):
            # Merged = (Shifting bit for allocating space) + LSB
            reverse_bit = (reverse_bit << 1) | (num & 1)

            # Discard LSB we get earlier
            num = num >> 1

        return reverse_bit


obj = Solution()
print(obj.reverseBits(43261596))      # 964176192
print(obj.reverseBits(2147483644))      # 1073741822

# T.C: O(1)
# S.C: O(1)