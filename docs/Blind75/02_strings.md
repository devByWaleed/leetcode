# Blind 75 Part 2: Strings

This part contains problems related to `Strings`, `Two-Pointers`, `Stack`, `HashMap`

`Total Count = 10`

---

## 1. LeetCode 125: Valid Palindrome (Easy)

* **Identified Pattern Upfront:** Two Pointers
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../strings/125.%20Valid%20Palindrome/`](../../strings/125.%20Valid%20Palindrome/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/valid-palindrome/submissions/2135871193)

### Code Solution

```python
class Solution:
    def isPalindrome(self, s):
        # New string
        cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        n = len(cleaned_text)

        # 2 Pointers
        left, right = 0, n - 1

        while left < right:
            # Checking for palindrome
            if cleaned_text[left] != cleaned_text[right]:
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
* **Solution Folder:** [`../../strings/242.%20Valid%20Anagram/`](../../strings/242.%20Valid%20Anagram/)
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

## 1. LeetCode No.: Name (Difficulty)

* **Identified Pattern Upfront:** 
* **Time Taken:**  minutes
* **Solution Folder:** [`../../`](../../)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
```