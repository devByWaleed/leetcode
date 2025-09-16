class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Hash_maps to store frequencies of both strings
        mag_freq = {}
        ransome_freq = {}

        # Counting frequencies of each char in magazine
        for i in magazine:

            if i not in mag_freq:

                mag_freq.update({i: 0})
            
            mag_freq[i] += 1


        # Counting frequencies of each char in ransomeNote
        for char in ransomNote:
        
            if char not in ransome_freq:

                ransome_freq.update({char: 0})
            
            ransome_freq[char] += 1


        # Checking that ransomeNote can be made from frequencies of magazine 
        for j in ransome_freq:

            if j not in mag_freq or mag_freq[j] < ransome_freq[j]:
                return False
            
        # After loop ends and find it, return True
        return True
        

obj = Solution()
print(obj.canConstruct("a", "b"))       # False
print(obj.canConstruct("aa", "ab"))     # False
print(obj.canConstruct("aa", "aab"))    # True
print(obj.canConstruct("aab", "baa"))   # True

# T.C: O(M + N)
# S.C: O(1)