from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)

        hash_map = {}

        # Loop to update the hashmap
        for i in range(n):

            hash_map.update({heights[i]: names[i]})
        
        # Sorting the hash_map  in descending order by key
        hash_map = dict(sorted(hash_map.items(), key=lambda item: item[0], reverse=True))


        # enumerate() to get index
        for index, key in enumerate(hash_map):
            
            # Sort the names array according to hash_map
            names[index] = hash_map[key]
            
            # Line for checking the height (debugging)
            # heights[index] = key
            

        return names


obj = Solution()
print(obj.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))    # ["Mary", "Emma", "John"]
print(obj.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))     # ["Bob", "Alice", "Bob"]

# T.C: O(N Log N)
# S.C: O(N)