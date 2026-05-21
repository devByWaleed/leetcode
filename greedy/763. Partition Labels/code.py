from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        
        # Edge case
        if n == 1:
            return [1]
        
        # Final answer array
        size = []

        # Keep track of current partition size
        curr_size = 0

        # Last position of every letter
        last = {x:i for i, x in enumerate(s)}
        # Window for 1st letter
        window = last[s[0]]

        i = 0

        while i < n:
            # Increment size
            curr_size += 1
            # Get last index
            last_pos = last[s[i]]

            # Window update
            if window < last_pos:
                window = last_pos


            # Get partition size
            if i == window:
                size.append(curr_size)
                curr_size = 0
                window = 0

            # Increase loop counter 
            i += 1

        return size


obj = Solution()
print(obj.partitionLabels("ababcbacadefegdehijhklij"))      # [9, 7, 8]
print(obj.partitionLabels("eccbbbbdec"))                    # [10]
print(obj.partitionLabels("ababcc"))                        # [4, 2]
print(obj.partitionLabels("caedbdedda"))                    # [1, 9]
print(obj.partitionLabels("eaaaabaaec"))                    # [9, 1]

# T.C: O(N)
# S.C: O(1)