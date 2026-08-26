class Solution:
    def canWinNim(self, n: int) -> bool:
        stones = n

        # Your turn
        remainder = stones % 4
        
        # If stones are multiple of 4, no chance to win
        if remainder == 0:
            return False
        
        # Removing stones
        stones -= remainder

        # If You remove last stone
        if stones == 0:
            return True
        
        # If n is a multiple of 4, that means opponent fwill fall into the trap.
        return True


obj = Solution()
print(obj.canWinNim(4))  # Output: False
print(obj.canWinNim(1))  # Output: True
print(obj.canWinNim(2))  # Output: True
print(obj.canWinNim(5))  # Output: True


'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        # If stones are multiple of 4, no chance to win
        return n % 4 != 0
            

obj = Solution()
print(obj.canWinNim(4))  # Output: False
print(obj.canWinNim(1))  # Output: True
print(obj.canWinNim(2))  # Output: True
print(obj.canWinNim(5))  # Output: True
'''



# Logically correct, but TLE
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        stones = n

        def removing_stone(stones):
            remainder = stones % 4

            # Some chances to win, so remove 1 stone
            if remainder == 0:
                return 1
            # Opponent will fall in multiple of 4 trap
            else:
                return remainder


        while stones > 0:
            player = removing_stone(stones)
            stones = stones - player

            # If Player remove last stone
            if stones == 0:
                return True
            
            friend = removing_stone(stones)
            stones = stones - friend

            # If Friend remove last stone
            if stones == 0:
                return False
            

obj = Solution()
print(obj.canWinNim(4))  # Output: False
print(obj.canWinNim(1))  # Output: True
print(obj.canWinNim(2))  # Output: True
print(obj.canWinNim(5))  # Output: True
'''