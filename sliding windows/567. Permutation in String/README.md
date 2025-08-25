# 567. Permutation in String

Given two strings `s1` and `s2`, return `true` if s2 contains a permutation of s1, or `false` otherwise.

> In other words, return `true` if one of `s1's permutations` is the `substring of s2`.
 

### Example 1

Input `s1 = ab, s2 = eidbaooo`

Output `true`

> Explanation **s2** contains one permutation of **s1 (ba)**.


### Example 2

Input `s1 = ab, s2 = eidboaoo`

Output `false`
 

### Constraints

`1 <= s1.length, s2.length <= 10^4`

`s1 and s2 consist of lowercase English letters.`


### Topics
- Hash Table
- Two Pointers
- String
- Sliding Window

---

### Hint 1
Obviously, brute force will result in `TLE(Time Limit Exceeded)`. Think of something else.

### Hint 2
How will you check whether one string is a permutation of another string?

### Hint 3
One way is to sort the string and then compare. But, Is there a better way?

### Hint 4
If one string is a permutation of another string then they must have one common metric. What is that?

### Hint 5
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?

### Hint 6
What about hash table? An `array of size 26`?