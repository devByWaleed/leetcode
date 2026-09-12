# Blind 75 Part 2: Strings

This part contains problems related to `Strings`, `Two-Pointers`, `Stack`, `HashMap`

`Total Count = 10`

---

## 1. LeetCode 125: Valid Palindrome (Easy)

* **Identified Pattern Upfront:** Two Pointers
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../String/125.%20Valid%20Palindrome/`](../../String/125.%20Valid%20Palindrome/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/valid-palindrome/submissions/2135871193)

### Code Solution

```python
class Solution:
    def isPalindrome(self, s):
        # New string
        # cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        # n = len(cleaned_text)

        n = len(s)
        # 2 Pointers
        left, right = 0, n - 1

        while left < right:
            # If left pointer encounter non-alphanumeric chars
            if not s[left].isalnum() or s[left] == " ":
                left += 1
                continue

            # If right pointer encounter non-alphanumeric chars
            if not s[right].isalnum() or s[right] == " ":
                right -= 1
                continue
            # Checking for palindrome
            if s[left].lower() != s[right].lower():
                return False
            else:
                # Pointer movement
                left += 1
                right -= 1

        # String in palindrome
        return True

        
obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal:Panama"))    # True
print(obj.isPalindrome(" "))                                # True
print(obj.isPalindrome("race a car"))                       # False
print(obj.isPalindrome("0P"))                               # False

# T.C: O(N)     —> Looping through string
# S.C: O(1)     —> No data structure used
```

---

## 2. LeetCode 20: Valid Parenthesis (Easy)

* **Identified Pattern Upfront:** Stack
* **Time Taken:** 10 minutes
* **Solution Folder:** [`../../stack/20.%20Valid%20Parentheses/`](../../stack/20.%20Valid%20Parentheses/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/valid-parentheses/submissions/2135913256)

### Code Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for verifying pair
        stack = []

        for i in range(len(s)):
            # For opening
            if s[i] == "(" or s[i] ==  "{" or s[i] ==  "[":
                stack.append(s[i])
            else:
                if stack:
                    top = stack.pop()
                    
                    # Pair Matching
                    if (
                        (top == "(" and s[i] == ")") or 
                        (top == "{" and s[i] == "}") or 
                        (top == "[" and s[i] == "]")
                    ):
                        continue
                    else:
                        # No matching pair
                        return False
                # Stack is empty
                else:
                    return False


        # If stack is empty, parenthesis is valid
        return False if stack else True

        
obj = Solution()
print(obj.isValid("()"))        # True
print(obj.isValid("()[]{}"))    # True
print(obj.isValid("(]"))        # False
print(obj.isValid("([])"))      # True
print(obj.isValid("([)]"))      # False

# T.C: O(N)     —> Looping through string
# S.C: O(1)     —> Stack data structure used
```

---

## 3. LeetCode 242: Valid Anagram (Easy)

* **Identified Pattern Upfront:** HashMap / Frequency-Table
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../String/242.%20Valid%20Anagram/`](../../String/242.%20Valid%20Anagram/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/valid-anagram/submissions/2135945041)

### Code Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: Different length
        if len(s) != len(t):
            return False

        hash_map = {}

        # Storing frequencies
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        for c in t:
            # If not in HashMap, then no anagram
            if c not in hash_map:
                return False
            else:
                # If frequency is 1, delete
                if hash_map[c] == 1:
                    del hash_map[c]

                # Else decrement frequency
                else:
                    hash_map[c] -= 1

        # t is anagram of s
        return True

        
obj = Solution()
print(obj.isAnagram("anagram", "nagaram"))      # True
print(obj.isAnagram("rat", "car"))              # False

# T.C: O(N)     —> Looping through string
# S.C: O(1)     —> HashMap data structure used, but will be empty if t is anagram. Plus all lowercase (26) english chars is far low than 128 possible combinations in ASCII.

# Follow-up: For Unicode, approach will be same. But the space complexity increases from O(1) to O(min(N, Σ)). Where Σ is unicode-set length and N is length of s
```

---

## 4. LeetCode 3: Longest Substring Without Repeating Characters (Medium)

* **Identified Pattern Upfront:** Sliding Window / HashSet
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../Sliding-Window/3.%20Longest%20Substring%20Without%20Repeating%20Characters/`](../../Sliding-Window/3.%20Longest%20Substring%20Without%20Repeating%20Characters/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2137154835)

### Code Solution

```python
# Using Hash-set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hash_set = set()

        left = 0

        for right in range(len(s)):
            # Shrinking window
            while s[right] in hash_set:
                # Removing from left side and adjusting window
                hash_set.remove(s[left])
                left += 1

            # Add to set
            hash_set.add(s[right])

            # Current window
            window = right - left + 1

            # Update with maximum
            max_length = max(max_length, window)

        return max_length


obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))       # 3
print(obj.lengthOfLongestSubstring("abcabcbb"))     # 3
print(obj.lengthOfLongestSubstring("bbbbb"))        # 1
print(obj.lengthOfLongestSubstring("aab"))          # 2
print(obj.lengthOfLongestSubstring("dvdf"))         # 3

# T.C: O(N)     --> Looping through string
# S.C: O(1)     --> HashSet used, but it never holds more than 1 same character
```

---

## 5. LeetCode 424: Longest Repeating Character Replacement (Medium)

* **Identified Pattern Upfront:** Sliding window / HAshMap
* **Time Taken:** 30 minutes
* **Solution Folder:** [`../../Sliding-Window/424.%20Longest%20Repeating%20Character%20Replacement/`](../../Sliding-Window/424.%20Longest%20Repeating%20Character%20Replacement/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/longest-repeating-character-replacement/submissions/2137208351)

### Code Solution

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Store maximum frequency
        max_freq = 0

        # Store final answer
        max_length = 0

        frequencies = {}

        left = 0


        for right in range(len(s)):
            # Add to map
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1

            # Update maximum frequency from MAP
            max_freq = max(max_freq, frequencies[s[right]])

            # Shrinking the window: If replacement needed
            while (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left += 1

            # Update with maximum
            max_length = max(max_length, right - left + 1)

        return max_length


obj = Solution()
print(obj.characterReplacement("ABAB", 2))      # 4
print(obj.characterReplacement("AABABBA", 1))   # 4
print(obj.characterReplacement("AAAA", 2))      # 4
print(obj.characterReplacement("ABAA", 0))      # 2

# T.C: O(N)     --> Looping through string
# S.C: O(1)     --> HashMap used, but it only holds maximum 26 chars i.e., constant overall
```

---

## 6. LeetCode 49: Group Anagrams (Medium)

* **Identified Pattern Upfront:** Sorting / HashMap
* **Time Taken:** 28 minutes
* **Solution Folder:** [`../../Hashing/49.%20Group%20Anagrams/`](../../Hashing/49.%20Group%20Anagrams/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/group-anagrams/submissions/2137236688)

### Code Solution

```python
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Base case
        if len(strs) == 1:
            return [strs]

        # Store final answer
        result = []

        # To store anagrams
        anagram_map = {}


        for ang in strs:
            # Create sorted string for checking anagram
            sorted_string = "".join(sorted(ang))

            # Initializing array to store anagrams / add the pair
            anagram_map[sorted_string] = anagram_map.get(sorted_string, [])

            # Add to respective key
            anagram_map[sorted_string].append(ang)

        # Adding anagrams-array to result
        for i in anagram_map.values():
            result.append(i)

        return result
    
        
# Answer can be in any order (order of the grouped anagrams or result array)
obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))     # [["bat"], ["nat","tan"], ["ate","eat","tea"]]
print(obj.groupAnagrams([""]))                                           # [[""]]
print(obj.groupAnagrams(["a"]))                                          # [["a"]]

# T.C: O(N * KLogK)     --> Looping through N elements with sorting each element of K length
# S.C: O(N * K)         --> HashMap used for storing sorted pairs array for N elements
```

---

## 7. LeetCode 76: Minimum Window Ssubstring (Hard)

* **Identified Pattern Upfront:** Sliding Window
* **Time Taken:** 44 minutes
* **Solution Folder:** [`../../Sliding-Window/76.%20Minimum%20Window%20Substring/`](../../Sliding-Window/76.%20Minimum%20Window%20Substring/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/minimum-window-substring/submissions/2138185144)

### Code Solution

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Cases
        if len(t) > len(s) :   return ""

        # Store frequencies of t'chars
        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Store substrings
        window = {}

        # have track the occurences of s in t
        # need is the total frequencies of t
        have, need = 0, len(count_t.keys())

        # Store final answer
        min_len = float("inf")

        # Pointers to track sub-string from s
        min_l, min_r = 0, 0

        # for window shrinking
        left = 0

        # For window expanding
        for right in range(len(s)):
            char = s[right]

            # Update window
            window[char] = window.get(char, 0) + 1

            # Update on finding t's char
            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    # Update minimum length & pointers for s
                    min_len = right - left + 1
                    min_l = left
                    min_r = right

                # Shrinking window
                left_char = s[left]
                window[left_char] -= 1
                left += 1

                # Decrement count for validation of window
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
            

        # +1 will add last index element
        return "" if min_len == float("inf") else s[min_l: min_r+1]


obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))        # BANC
print(obj.minWindow("a", "a"))                      # a
print(obj.minWindow("a", "aa"))                     # ""

# T.C: O(M + N)     --> Loop through string "t" + "s"
# S.C: O(K)         --> HashMap used to store K size window
```

---

## 8. LeetCode 647: Palindromic Substrings (Medium)

* **Identified Pattern Upfront:** Two-Pointers / DP
* **Time Taken:** 17 minutes
* **Solution Folder:** [`../../Two-Pointers/647.%20Palindromic%20Substrings/`](../../Two-Pointers/647.%20Palindromic%20Substrings/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/palindromic-substrings/submissions/2139207859)

### Code Solution

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # Count all substrings
        total_palindrome = 0

        def expand_towards_center(i, j):
            # Return total count
            count = 0

            # Index Inbound & palindrome checking
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1

                # Expanding towards center
                i -= 1
                j += 1

            return count

        
        for i in range(n):
            # Odd length center
            total_palindrome += expand_towards_center(i, i)

            # Even length center
            total_palindrome += expand_towards_center(i, i+1)

        # Final count
        return total_palindrome


obj = Solution()
print(obj.countSubstrings("abc"))       # 3
print(obj.countSubstrings("aaa"))       # 6

# T.C: O(N ^ 2)     --> Nested looping
# S.C: O(1)         --> No data structure used
```

---

## 9. LeetCode 5: Longest Palindromic Substrings (Medium)

* **Identified Pattern Upfront:** Two-Pointers / DP
* **Time Taken:** 17 minutes
* **Solution Folder:** [`../../Two-Pointers/5.%20Longest%20Palindromic%20Substring/`](../../Two-Pointers/5.%20Longest%20Palindromic%20Substring/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/longest-palindromic-substring/submissions/2139243834)

### Code Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        
        # Count all substrings
        res = ""
        res_len = 0

        def expand_towards_center(i, j):
            nonlocal res, res_len

            # Index Inbound & palindrome checking
            while i >= 0 and j < n and s[i] == s[j]:
                # Check if current one is longer than already set
                if j - i + 1 > res_len:
                    res = s[i : j + 1]
                    res_len = j - i + 1

                # Expanding towards center
                i -= 1
                j += 1


        for i in range(n):
            # Odd length center
            expand_towards_center(i, i)

            # Even length center
            expand_towards_center(i, i+1)

        # Final string
        return res


obj = Solution()
print(obj.longestPalindrome("babad"))       # 3
print(obj.longestPalindrome("cbbd"))       # 6
print(obj.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

))       # 489

# T.C: O(N ^ 2)     --> Nested looping
# S.C: O(1)         --> No data structure used
```

---

## 10. LeetCode 271: Encode and Decode Strings (Medium)

* **Identified Pattern Upfront:** Design / String
* **Time Taken:** 14 minutes
* **Solution Folder:** [`../../Design/271.%20Encode%20and%20Decode%20Strings/`](../../Design/271.%20Encode%20and%20Decode%20Strings/)
* **Submittion Link:** Solved on NeetCode

### Code Solution

```python
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoded string
        encoded_s = ""

        # Encoding structure: Length + # + String
        for s in strs:
            encoded_s += f"{len(s)}#{s}"
        
        return encoded_s


    def decode(self, s: str) -> List[str]:
        # Final answer array
        result = []

        # Pointer for iteration
        i = 0
        while i < len(s):
            # Pointer to find "#"
            j = i

            while s[j] != "#":
                j += 1

            # When "#" finds, extract length
            length = int(s[i:j])

            # Extract word, length will be excluded
            word = s[j + 1 : j + 1 + length]

            # Add to result
            result.append(word)

            # Move pointer i to move towards next word
            i = j + 1 + length

        return result


obj = Solution()
l1 = obj.encode(["Hello","World"])
print(obj.decode(l1))       # ["Hello","World"]
l2 = obj.encode([""])
print(obj.decode(l2))       # [""]

# T.C: O(N)     --> Looping through array / string for encode() & decode()
# S.C: O(N)     --> N length string / array for encode() & decode()
```











---

## 1. LeetCode No.: Name (Difficulty)

* **Identified Pattern Upfront:** 
* **Time Taken:**  minutes
* **Solution Folder:** [`../../`](../../)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
```