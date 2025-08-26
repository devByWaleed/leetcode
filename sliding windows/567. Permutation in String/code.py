class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        frequencies = {}    # Store frequencies of s1

        window_freq = {}    # Store frequencies of current window

        for i in s1:
            
            if i not in frequencies:
                frequencies.update({i: 0})
            
            frequencies[i] += 1


        # Storing frequencies of 1st "s1.length" size window
        window = s2[:len(s1)]

        for j in window:
            
            if j not in window_freq:
                window_freq[j] = 0
            
            window_freq[j] += 1


        # Looping over remaining string
        for j in range(len(s1), len(s2)):
            
            # If permutation found, return true
            if frequencies == window_freq:
                return True
            # Else remove leftmost element
            window_freq[s2[j-len(s1)]] -= 1

            # Edge case for removal of character
            if window_freq[s2[j-len(s1)]] == 0:
                window_freq.pop(s2[j-len(s1)])
            
            # Add current's frequency
            window_freq[s2[j]] = window_freq.get(s2[j], 0) + 1


        # After whole loop, compare both hashmaps
        return frequencies == window_freq


obj = Solution()
print(obj.checkInclusion("ab", "eidbaooo"))     # True
print(obj.checkInclusion("ab", "eidboaoo"))     # False
print(obj.checkInclusion("a", "ab"))            # True
print(obj.checkInclusion("adc", "dcda"))        # True

# T.C: O(N)
# S.C: O(1)