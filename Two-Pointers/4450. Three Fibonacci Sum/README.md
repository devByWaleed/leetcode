# 4450. Three Fibonacci Sum

**Link:** [https://leetcode.com/problems/three-fibonacci-sum/description/](https://leetcode.com/problems/three-fibonacci-sum/description/)

---

You are given an integer `n`.

The **Fibonacci sequence** starts with 0 and 1, and each subsequent number is
the sum of the previous two numbers. Its first few terms are `0, 1, 1, 2, 3,
5, 8, 13, ...`.

Return `true` if `n` can be expressed as the sum of **three consecutive
terms** in the Fibonacci sequence, and `false` otherwise.



**Example 1:**

**Input:** n = 16

**Output:** true

**Explanation:**

The three consecutive terms 3, 5, and 8 have a sum of `3 + 5 + 8 = 16`.

**Example 2:**

**Input:** n = 8

**Output:** false

**Explanation:**

Although `1 + 2 + 5 = 8`, these terms are not consecutive in the Fibonacci
sequence. No three consecutive terms have a sum of 8.

**Example 3:**

**Input:** n = 2

**Output:** true

**Explanation:**

The first three terms have a sum of `0 + 1 + 1 = 2`.



**Constraints:**

  * `1 <= n <= 109`


---

### Hint 1
**1a (Sequence Generation)** : Generate consecutive Fibonacci triples and
compare their sums with `n`. Stop when the sum exceeds `n`.

### Hint 2
**2a (Fibonacci Identity)** : For consecutive Fibonacci terms `a`, `b`, and
`c`, we have `a + b == c`, so their sum is `2 * c`.

### Hint 3
**2b (Fibonacci Identity)** : Thus, `n` must be even and `n / 2` must be a
positive Fibonacci number.

### Hint 4
**2c (Fibonacci Identity)** : A positive integer `x` is Fibonacci exactly when
`5 * x * x + 4` or `5 * x * x - 4` is a perfect square.
