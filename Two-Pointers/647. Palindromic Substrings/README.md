# 647. Palindromic Substrings

Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

## Examples

**Example 1:**
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Topics
- String
- Dynamic Programming
- Two Pointers

---

## Hints
1. How can we reuse a previously computed palindrome to compute a larger one?
2. If "aba" is a palindrome, is "xabax" a palindrome? Similarly is "xabay" a palindrome?
3. Complexity based hint: If we use brute-force and check whether for every start and end position a substring is a palindrome, we have O(n^2) start-end pairs and O(n) palindromic checks, resulting in O(n^3) time complexity. Can we reduce the time complexity of palindromic checks to O(1) by reusing some previous computation?