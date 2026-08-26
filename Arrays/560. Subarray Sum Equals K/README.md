# 560. Subarray Sum Equals K

## Problem Description

Given an array of integers `nums` and an integer `k`, return the *total number of subarrays whose sum equals to* `k`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

### Examples

**Example 1:**

```text
Input: nums = [1,1,1], k = 2
Output: 2

```

**Example 2:**

```text
Input: nums = [1,2,3], k = 3
Output: 2

```

### Constraints

* $1 \le \text{nums.length} \le 2 \times 10^4$
* $-1000 \le \text{nums}[i] \le 1000$
* $-10^7 \le k \le 10^7$

### Topics
- Senior Staff
- Array
- Hash Table
- Prefix Sum

---

### Hint 1
Will Brute force work here? Try to optimize it.

### Hint 2
Can we optimize it by using some extra space?

### Hint 3
What about storing sum frequencies in a hash table? Will it be useful?

### Hint 4
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.