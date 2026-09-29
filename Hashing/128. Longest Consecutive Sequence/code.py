from typing import List

# Using Union find (DSU)
class DynamicDisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def findParent(self, node):
        #  If node is seen for the first time, initialize it
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1

        # Base case: node is its own ultimate parent
        if node == self.parent[node]:
            return node
        
        # Path Compression: point directly to the ultimate parent
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        root_u = self.findParent(u)
        root_v = self.findParent(v)

        # If already in the same component, return the size
        if root_u == root_v:
            return self.size[root_u]

        # Attach smaller tree under the larger tree
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
            return self.size[root_v]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
            return self.size[root_u]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case for empty array
        if not nums:
            return 0
        
        # Edge case for 1 element array
        if len(nums) == 1:
            return 1
        
        # Convert the input list to a set for O(1) lookups and to remove duplicates.
        hash_set = set(nums)

        # Initialize disjoint set
        dsu = DynamicDisjointSet()

        # Store longest consecutive sequence.
        max_longest = 0

        for num in hash_set:
            dsu.findParent(num)

            if num + 1 in hash_set:
                # Unoin by size
                curr_size = dsu.unionBySize(num, num+1)

                max_longest = max(max_longest, curr_size)
            else:
                # This is start of sequence
                max_longest = max(max_longest, 1)

        return max_longest


obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))                   # 4
print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))           # 9
print(obj.longestConsecutive([1, 0, 1, 2]))                             # 3
print(obj.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))      # 7
print(obj.longestConsecutive([1, 2, 0, 1]))                             # 3
print(obj.longestConsecutive([0]))                                      # 1
print(obj.longestConsecutive([0, 0]))                                   # 1
print(obj.longestConsecutive([]))                                       # 0

# T.C: O(Nα(N))     --> Inverse Ackermann function + Looping on N unique numbers
# S.C: O(N)         --> Hashset used for Pointers, sizes, N uniques numbers





# Using Hash-Set
'''
# - Add edge cases to tackle smallest constraints
# - According to description, nothing to do with redundant number. Hence  create a hash_set for constant lookup on unique numbers. This is sorted in ascending order.
# - If previous number is present, we know streak will not be increase. If we add it, it will be redundant. 
# - If not present, we can start our streak and go on to the numbers which are present in set, inside while loop. If next number is not present, we come to know that it's next number will also not in set as it is consecutive sequence.
# - After while loop, just update streak with longest sequence by checking maximum number. After loop, return it.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case for empty array
        if len(nums) == 0:
            return 0
        
        # Edge case for 1 element array
        if len(nums) == 1:
            return 1
        
        # Convert the input list to a set for O(1) lookups and to remove duplicates.
        hash_set = set(nums)

        # Store longest consecutive sequence.
        longest = 0

        for num in hash_set:

            # If num is start of sequence or not
            if num - 1 not in hash_set:
                streak = 1      # streak to keep track of longest sequence

                # Incrementing the loop number & streak while the num is in set
                while num + 1 in hash_set:
                    streak += 1
                    num += 1

                # Updating the longest sequence by longest streak
                longest = max(longest, streak)

        return longest


obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))                   # 4
print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))           # 9
print(obj.longestConsecutive([1, 0, 1, 2]))                             # 3
print(obj.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))      # 7
print(obj.longestConsecutive([1, 2, 0, 1]))                             # 3
print(obj.longestConsecutive([0]))                                      # 1
print(obj.longestConsecutive([0, 0]))                                   # 1
print(obj.longestConsecutive([]))                                       # 0

# T.C: O(N)
# S.C: O(N)
'''