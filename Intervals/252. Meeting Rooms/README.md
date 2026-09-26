## 1. Meeting Rooms (LeetCode 252)

### Description

Given an array of meeting time intervals consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` (`start_i < end_i`), determine if a person could attend all meetings without any conflicts.

> **Note:** `(0,8),(8,10)` is NOT considered a conflict at `8`.

### Test-Cases

* **Example 1:**
* **Input:** `intervals = [(0,30),(5,10),(15,20)]`
* **Output:** `false`


* **Example 2:**
* **Input:** `intervals = [(5,8),(9,15)]`
* **Output:** `true`


* **Example 3:**
* **Input:** `intervals = [(0,8),(8,10)]`
* **Output:** `true`



### Topics

* Array
* Sorting

### Hints

1. If you process meetings in chronological order, when can two meetings overlap?
2. Sort the intervals by their start times.
3. Check if the start time of the current meeting is strictly less than the end time of the previous meeting.

### Recommended Complexity

* **Time Complexity:** $\mathcal{O}(N \log N)$
* **Space Complexity:** $\mathcal{O}(1)$ or $\mathcal{O}(N)$ depending on the sorting algorithm implementation