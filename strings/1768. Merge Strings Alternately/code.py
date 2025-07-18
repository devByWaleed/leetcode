class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Edge Cases
        if len(word1) == 0: return word2
        if len(word2) == 0: return word1

        merged = ''

        # 2 Pointers to traverse both strings
        left, right = 0, 0

        len1 = len(word1)
        len2 = len(word2)

        
        # while left < len(word1) and right < len(word2):
        while left < len1 or right < len2:

            # Conditions to check length then add character
            if left != len1:
                merged += word1[left]
                left += 1
            
            # Conditions to check length then add character
            if right != len2:
                merged += word2[right]
                right += 1


        return merged


obj = Solution()
print(obj.mergeAlternately("abc", "pqr"))       # apbqcr
print(obj.mergeAlternately("ab", "pqrs"))       # apbqrs
print(obj.mergeAlternately("abcd", "pq"))       # apbqcd

# T.C: O(M + N)
# S.C: O(1)


'''
if len(word1) == len(word2):

            while left < len(word1):
                merged += word1[left]
                merged += word2[right]

                left += 1
                right += 1
            
            return merged
        
        elif len(word1) < len(word2):

            while left != len(word1):

                merged += word1[left]
                merged += word2[right]

                if left < len(word1):  left += 1

                right += 1
            
            return merged
        
        elif len(word2) < len(word1):

            while left != len(word2):

                merged += word1[left]
                merged += word2[right]

                if right < len(word2):  right += 1

                left += 1
            
            return merged
'''