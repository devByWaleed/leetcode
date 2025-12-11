class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)     # Winodw size

        # Edge case
        if k > len(s2):    return False
    
        frequency = {}      # Frequency of string to be checked
        freq_window = {}    # Frequenc of chars in current window

        # Storing frequency of s1
        for i in range(k):
            frequency[s1[i]] = frequency.get(s1[i], 0) + 1

        # Storign frequency of first k element
        for i in range(k):
            freq_window[s2[i]] = freq_window.get(s2[i], 0) + 1

        left = 0    # For shrinking window

        # Looping through rest of string
        for right in range(k, len(s2)):

            # Checking for frequency count
            if frequency == freq_window:
                return True
            
            # Expanding and shrinking window
            freq_window[s2[right]] = freq_window.get(s2[right], 0) + 1
            if freq_window[s2[left]] > 1:   freq_window[s2[left]] -= 1
            else:   del freq_window[s2[left]]
            left += 1


        return frequency == freq_window    # For final check


obj = Solution()
print(obj.checkInclusion("ab", "eidbaooo"))     # True
print(obj.checkInclusion("ab", "eidboaoo"))     # False
print(obj.checkInclusion("a", "ab"))            # True
print(obj.checkInclusion("adc", "dcda"))        # True

# T.C: O(N)
# S.C: O(1)