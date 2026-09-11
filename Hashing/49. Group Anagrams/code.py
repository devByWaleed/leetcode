from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Base case
        if len(strs) == 1:
            return [strs]

        # Store final answer
        result = []

        # To store anagrams
        anagram_map = {}


        for ang in strs:
            # Create sorted string for checking anagram
            sorted_string = "".join(sorted(ang))

            # Initializing array to store anagrams / add the pair
            anagram_map[sorted_string] = anagram_map.get(sorted_string, [])

            # Add to respective key
            anagram_map[sorted_string].append(ang)

        # Adding anagrams-array to result
        for i in anagram_map.values():
            result.append(i)

        return result
    
        
# Answer can be in any order (order of the grouped anagrams or result array)
obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))     # [["bat"], ["nat","tan"], ["ate","eat","tea"]]
print(obj.groupAnagrams([""]))                                           # [[""]]
print(obj.groupAnagrams(["a"]))                                          # [["a"]]

# T.C: O(N * KLogK)     --> Looping through N elements with sorting each element of K length
# S.C: O(N * K)         --> HashMap used for storing sorted pairs array for N elements