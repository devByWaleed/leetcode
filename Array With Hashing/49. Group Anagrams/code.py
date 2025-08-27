from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Edge Case for only 1 element
        if len(strs) == 1:
            return [strs]


        anagram_map = {}

        # Array to store final pair
        result = []

        for strings in strs:

            # Creating a copy then sorted it
            sorted_str = strings
            sorted_str = "".join(sorted(sorted_str))

            # Updating the hashmap with sorted one as key and iterators as value inside []
            anagram_map[sorted_str] = anagram_map.get(sorted_str, [])
            anagram_map[sorted_str].append(strings)

        # Appending the pairs in result array
        for pair in reversed(anagram_map.values()):
            result.append(pair)

        return result


# Answer can be in any order (order of the grouped anagrams or result array)
obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))     # [["bat"], ["nat","tan"], ["ate","eat","tea"]]
print(obj.groupAnagrams([""]))                                           # [[""]]
print(obj.groupAnagrams(["a"]))                                          # [["a"]]

# T.C: O(N * KLogK)
# S.C: O(N * K)