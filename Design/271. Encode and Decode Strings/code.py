from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoded string
        encoded_s = ""

        # Encoding structure: Length + # + String
        for s in strs:
            encoded_s += f"{len(s)}#{s}"
        
        return encoded_s


    def decode(self, s: str) -> List[str]:
        # Final answer array
        result = []

        # Pointer for iteration
        i = 0
        while i < len(s):
            # Pointer to find "#"
            j = i

            while s[j] != "#":
                j += 1

            # When "#" finds, extract length
            length = int(s[i:j])

            # Extract word, length will be excluded
            word = s[j + 1 : j + 1 + length]

            # Add to result
            result.append(word)

            # Move pointer i to move towards next word
            i = j + 1 + length

        return result


obj = Solution()
l1 = obj.encode(["Hello","World"])
print(obj.decode(l1))       # ["Hello","World"]
l2 = obj.encode([""])
print(obj.decode(l2))       # [""]

# T.C: O(N)     --> Looping through array / string for encode() & decode()
# S.C: O(N)     --> N length string / array for encode() & decode()