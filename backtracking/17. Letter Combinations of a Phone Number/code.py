from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        
        # Base case
        if n == 0:  return []

        # Store all combinations
        result = []

        # Currnt combinations
        pair = []

        # Mapping
        letter_map = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i):
            # If we get combination
            if i == n:
                result.append("".join(pair))
                return

            for letter in letter_map[digits[i]]:
                # Add letter
                pair.append(letter)

                # Call for next element
                backtrack(i+1)

                # UNDO the step
                pair.pop()

        
        # Call bactrack function for 1st element
        backtrack(0)
        return result


obj = Solution()

print(obj.letterCombinations("23"))     # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(obj.letterCombinations("2"))      # ["a","b","c"]

# T.C: O(4^N)
# S.C: O(N)