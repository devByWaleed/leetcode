class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Hash map to store frequencies of chars
        hash_map = {}

        # Final String
        sort_chars = ""

        # Loop to add frequencies
        for i in range(len(s)):

            if s[i] not in hash_map:
                hash_map.update({s[i]: 0})
            
            hash_map[s[i]] += 1
        
        # Sorting the hashmap with lambda function in decreasing order
        hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        # Looping on hashmap and add it to final string
        for i in hash_map:

            sort_chars += i * hash_map[i]

        return sort_chars


obj = Solution()
print(obj.frequencySort("tree"))                # eetr / eert
print(obj.frequencySort("cccaaa"))              # cccaaa / aaaccc
print(obj.frequencySort("Aabb"))                # bbAa / bbaA
print(obj.frequencySort("loveleetcode"))        # eeeeoollvtdc

# T.C: O(N Log N)
# S.C: O(N)