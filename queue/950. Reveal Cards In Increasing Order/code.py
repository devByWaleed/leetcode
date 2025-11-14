from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        n = len(deck)
        result = [None] * n

        deck.sort()

        i, j = 0, 0
        skip = False

        while i < n:

            if result[j] == None:
                if not skip:
                    result[j] = deck[i]
                    i += 1
                    skip = True
                else:
                    skip = False

            j = (j + 1) % n


        return result


obj = Solution()
print(obj.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))     # [2, 13, 3, 11, 5, 17, 7]
print(obj.deckRevealedIncreasing([1, 1000]))                    # [1, 1000]

# T.C: O(N LOG N)
# S.C: O(N)