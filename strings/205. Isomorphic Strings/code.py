class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # Edge Case for un-equal length
        if len(s) != len(t):    return False

        # Pointer for traversing on t
        pointer = 0

        # Hash map to store values to be checked
        hash_map = {}

        for i in s:

            # If values not in hashmap, then go to
            if i not in hash_map:

                # If the correspoding value is mapped before, return False
                if t[pointer] in hash_map.values():  return False  
                
                hash_map[i] = t[pointer]
                pointer += 1

            # If values in hashmap, check for mapping
            elif hash_map[i] == t[pointer]:
                pointer += 1
            
            # If apping is not same, return False
            else:
                return False
        
        # After whole loop, retur true as it is isomorphic string
        return True


obj = Solution()
print(obj.isIsomorphic("egg", "add"))       # True
print(obj.isIsomorphic("foo", "bar"))       # False
print(obj.isIsomorphic("paper", "title"))   # True
print(obj.isIsomorphic("badc", "baba"))     # False

# T.C: O(N)
# S.C: O(N)