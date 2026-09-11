class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        
        if n == 1:     return s     # Edge Case

        left = 0
        right = n - 1

        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = "aeiouAEIOU"

        # Coverting to list at start to encounter time limit exceed 
        char_list = list(s)

        while left < right:

            if s[left] in vowels and s[right] in vowels:
                """
                Swapping and convert to string 
                """
                char_list[left], char_list[right] = char_list[right], char_list[left]

                left += 1
                right -= 1
                
            # If both chars are not vowels
            elif s[left] not in vowels and s[right] not in vowels:
                left += 1
                right -= 1

            # If chars at left is not vowels
            elif s[left] not in vowels:
                left += 1

            # If chars at right is not vowels
            elif s[right] not in vowels:
                right -= 1
        
        s = "".join(char_list)  # Convering to the string before returning
        return s


obj = Solution()
print(obj.reverseVowels("IceCreAm"))    # AceCreIm
print(obj.reverseVowels("leetcode"))    # leotcede
print(obj.reverseVowels("race car"))    # race car

# T.C: O(N)
# S.C: 