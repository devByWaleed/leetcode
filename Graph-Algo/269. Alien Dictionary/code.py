from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize graph data structures
        # adj maps each character to a set of characters that come after it
        adj = {char: set() for word in words for char in word}
        # in_degree tracks the count of incoming edges for each unique character
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: Build the directed graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Edge Case: Prefix check (e.g., "abcd" comes before "abc")
            # An invalid dictionary where a longer word precedes its prefix
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            # Find the first character where the two words differ
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # word1[j] must come BEFORE word2[j] (edge: word1[j] -> word2[j])
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    # Only the first differing character gives us relative ordering
                    break

        # Step 3: Collect all nodes with 0 in-degree (no predecessors)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        res = []

        # Step 4: Process graph using BFS (Kahn's Algorithm)
        while queue:
            char = queue.popleft()
            res.append(char)

            # Decrease in-degree for all neighboring characters
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add neighbor to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Cycle Check
        # If the ordering includes all unique characters, return it.
        # Otherwise, a cycle was detected (invalid ordering) -> return ""
        if len(res) == len(in_degree):
            return "".join(res)
        else:
            return ""


obj = Solution()
print(obj.foreignDictionary(["z","o"]))                         # "zo"
print(obj.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))   # "hernf"
print(obj.foreignDictionary(["abc","ab"]))                      # ""

# T.C: O(N)     --> Looping over N nodes
# S.C: O(N)     --> Call-Stack for N nodes used