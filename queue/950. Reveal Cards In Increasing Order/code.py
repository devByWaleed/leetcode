from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        
        # Final array
        result = [None] * n

        # We have to reveal in increasing order
        deck.sort()

        i = 0   # For deck
        j = 0   # For result
        
        # To keep track of skipping
        skip = False

        # Until all cards are revealed
        while i < n:

            # If place is not filled
            if result[j] == None:
                if not skip:
                    result[j] = deck[i]
                    i += 1
                    # After revealing, the NEXT available slot must be skipped
                    skip = True
                else:
                    # SKIP: Leave this slot None (simulates moving card to bottom)
                    skip = False

            # Circular wrap-up
            j = (j + 1) % n


        return result


obj = Solution()
print(obj.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))     # [2, 13, 3, 11, 5, 17, 7]
print(obj.deckRevealedIncreasing([1, 1000]))                    # [1, 1000]

# T.C: O(N LOG N)
# S.C: O(N)