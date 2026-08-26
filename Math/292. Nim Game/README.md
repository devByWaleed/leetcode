# 292. Nim Game

## Problem Description

You are playing the following Nim Game with your friend:

* Initially, there is a heap of stones on the table.
* You and your friend take turns making a move, with **you starting first**.
* On each turn, the person whose turn it is can remove **1, 2, or 3 stones** from the heap.
* The one who removes the last stone is the winner.

Given `n`, the number of stones in the heap, return `True` if you can win the game assuming both you and your friend play optimally, otherwise return `False`.

### Examples

**Example 1:**

```text
Input: n = 4
Output: False
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes 1 stone, including the last stone. Your friend wins.
In all outcomes, your friend wins.

```

**Example 2:**

```text
Input: n = 1
Output: True

```

**Example 3:**

```text
Input: n = 2
Output: True

```

### Constraints

* $1 \le n \le 2^{31} - 1$

### Topics
- Math
- Brainteaser
- Minimax
- Game Theory
- Nim Game
- Impartial Game

---

### Hint 1
If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?