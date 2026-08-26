# 724. Find Pivot Index

## Problem Description

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly to the left** of the index is equal to the sum of all the numbers **strictly to the right** of the index.

* If the index is on the left edge of the array, the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.
* Return the **leftmost pivot index**. If no such index exists, return `-1`.

### Examples

**Example 1:**

```text
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

```

**Example 2:**

```text
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

```

**Example 3:**

```text
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + (-1) = 0

```

### Constraints

* $1 \le \text{nums.length} \le 10^4$
* $-1000 \le \text{nums}[i] \le 1000$

### Topics
- Mid Level
- Array
- Prefix Sum
- Weekly Contest 58

---

### Hint 1
Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.

### Hint 2
Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.

### Hint 3
For each index i, check if sumLeft[i] equals sumRight[i]. If so, return i. If no such i is found, return -1.