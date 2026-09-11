class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # No. of unique codes
        unique = 2 ** k

        # Hashset to track unique codes
        sub_strings = set()

        # Extracting 1st k size code and add its decimal value to set
        window_code = s[:k]

        current_num = int(window_code, 2)

        sub_strings.add(current_num)

        # Looping over remaining string
        for i in range(k, len(s)):

            # Dropping leftmost char and adding current one by using this formula
            new_num = ((current_num & ((1 << (k-1)) - 1)) << 1) | int(s[i])
            sub_strings.add(new_num)

            # Updating current number
            current_num = new_num

            # Early exit if we already found all codes
            if len(sub_strings) == unique:
                return True

        # Compairing unique sub-strings with 2^k
        return len(sub_strings) == unique


obj = Solution()
print(obj.hasAllCodes("00110110", 2))       # True
print(obj.hasAllCodes("0110", 1))           # True
print(obj.hasAllCodes("0110", 2))           # False

# T.C: O(N)
# S.C: O(2 ^ K)


# Brute Force
'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # No. of unique codes
        unique = 2 ** k


        # Hashset to track unique codes
        sub_strings = set()

        # Loop range for all sub-strings of k length
        for i in range(0, len(s)-k+1):

            sub = s[i: k+i]

            # If sub-string is unique, add to hashsset. Otherwise ignore
            if sub not in sub_strings:
                sub_strings.add(sub)
            else:
                continue
        
        # Length of hashset and unique (int) will check for all binary codes
        return len(sub_strings) == unique


obj = Solution()
print(obj.hasAllCodes("00110110", 2))       # True
print(obj.hasAllCodes("0110", 1))           # True
print(obj.hasAllCodes("0110", 2))           # False

# T.C: O(N * K)
# S.C: O(2 ^ K)
'''