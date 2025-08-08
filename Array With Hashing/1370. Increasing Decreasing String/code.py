class Solution:
    def sortString(self, s: str) -> str:
        
        n = len(s)
        frequency = {}

        # Final String
        result = ""

        for i in range(n):

            if s[i] not in frequency:

                frequency.update({s[i]: 0})
            
            frequency[s[i]] += 1

        # While looop to track how many time algo works
        while len(result) < n:

            # Loop from 'a' to 'z'
            for c in range(26):

                character = chr(ord('a') + c)

                # Conditions for adding char
                if character in s and frequency[character] != 0:
                
                    result += character
                    frequency[character] -= 1
            
            
            # Loop from 'z' to 'a'
            for c in range(25, -1, -1):

                character = chr(ord('a') + c)

                # Conditions for adding char
                if character in s and frequency[character] != 0:
                    result += character
                    frequency[character] -= 1


        return result


obj = Solution()
print(obj.sortString("aaaabbbbcccc"))   # abccbaabccba
print(obj.sortString("rat"))            # art

# T.C: O(N)
# S.C: O(1)