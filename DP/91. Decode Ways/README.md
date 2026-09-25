# 91. Decode Ways

## Problem Description

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the mapping:

```text
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

* `"AAJF"` with the grouping `(1 1 10 6)`
* `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return the **number of ways** to decode it. If the entire string cannot be decoded in any valid way, return `0`.

### Examples

**Example 1:**

```text
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

```

**Example 2:**

```text
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

```

**Example 3:**

```text
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

```

### Constraints

* $1 \le$ `s.length` $\le 100$
* `s` consists of only digits and may contain leading zero(s).

### Topics
- String
- Dynamic Programming
