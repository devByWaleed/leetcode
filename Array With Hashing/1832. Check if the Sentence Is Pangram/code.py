class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        hash_set = set()

        for i in sentence:

            # If not in hash_set, add
            if i not in hash_set:
                hash_set.add(i)
            
            # If in hash_set, ignore
            else:
                continue
        
        # Check for all alphabets length
        return len(hash_set) == 26


obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))    # True
print(obj.checkIfPangram("leetcode"))                               # False

# T.C: O(N)
# S.C: O(1)