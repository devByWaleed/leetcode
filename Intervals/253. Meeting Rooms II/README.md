## 2. Meeting Rooms II (LeetCode 253)

### Description

Given an array of meeting time intervals consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` (`start_i < end_i`), find the minimum number of rooms required to schedule all meetings without any conflicts.

> **Note:** `(0,8),(8,10)` is NOT considered a conflict at `8`.

### Test-Cases

* **Example 1:**
* **Input:** `intervals = [(0,40),(5,10),(15,20)]`
* **Output:** `2`


* **Example 2:**
* **Input:** `intervals = [(4,9)]`
* **Output:** `1`


* **Example 3:**
* **Input:** `intervals = [(1,10),(2,7),(3,19),(8,12),(10,20),(11,30)]`
* **Output:** `4`



### Topics

* Array
* Two Pointers
* Greedy
* Sorting
* Heap (Priority Queue)

### Hints

1. Think about how rooms get freed up—a room becomes available as soon as the meeting inside it ends.
2. If you sort meetings by start time, how can you efficiently keep track of the earliest ending meeting?
3. Consider using a Min-Heap to store the end times of ongoing meetings, or sort start and end times separately using two pointers.

### Recommended Complexity

* **Time Complexity:** $\mathcal{O}(N \log N)$
* **Space Complexity:** $\mathcal{O}(N)$