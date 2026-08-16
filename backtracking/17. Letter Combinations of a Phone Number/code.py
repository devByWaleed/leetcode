from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)

        # Mapping
        letter_map = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # Stores final answer
        result = []
        
        # Stores single pairs
        pairs = []
        
        def backtrack(i):
            # Base case to add into result
            if i == n:
                result.append("".join(pairs))
                return
            
            for letter in letter_map[digits[i]]:
                # Add to pairs
                pairs.append(letter)
                
                # Backtrack
                backtrack(i+1)
                
                # POP ( UNDO )
                pairs.pop()
        
        # Call function with initial value
        backtrack(0)
        return result


obj = Solution()
print(obj.letterCombinations("23"))     # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(obj.letterCombinations("2"))      # ["a","b","c"]

# T.C: O(4^N) --> Max mapping + Looking for each combination + creating copy
# S.C: O(N) --> Recursive call stack used