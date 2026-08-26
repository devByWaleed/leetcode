# Capstone: Pattern Journal + Timed Mock

## Part 1. Pattern Journal

**10 Patterns List:-**
1. Prefix Sum
1. Hash Map
1. Two Pointers
1. Sliding Window
1. Backtracking
1. Monotonic Stack
1. DFS/BFS
1. Binary Search
1. Top K Elements (Heaps)
1. Dynamic Programming

---

### Prefix Sum

#### Trigger Words
1. Prefix
1. Suffix
1. Running Sum
1. Minimum Number of Operations
1. Minimum Size
1. Subarray Sum
1. Product of Array
1. Largest Sum
1. answer[i]

#### Template

**Running Sum**
```python
# for loop starting from 2nd element as 1st one remains same
for i in range(1, len(nums)):

    # Updating the element by summing it with previous one
    nums[i] = nums[i] + nums[i-1]

return nums
```

**1D Prefix Sum Template**
```python
# Step 1: Build the prefix sum array (with 1-based padding for clean math)
n = len(nums)
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

# Step 2: Query sum of subarray from index L to R (inclusive)
def query_sum(left: int, right: int) -> int:
    return prefix[right + 1] - prefix[left]
```

---

### Hash Map

#### Trigger Words
- Hash-Map
    1. Frequency, Frequent Elements
    1. Mapping, Pattern
    1. Deep Copy, Copy List
    1. Element That Appears More Than
    1. Pair, Dictionary
- Hash-Set
    1. Without Repetition
    1. Contains Duplicate
    1. 

#### Template

**Frequency Map Template**
```python
freq = {}

for ch in data:
    freq[ch] = freq.get(ch, 0) + 1
```

**HashSet (Visited Detection)**
```python
seen = set()

for x in data:
    if x in seen:
        return True
    seen.add(x)
```

**HashSet Cleanup Pattern**

```python
if x in seen:
    seen.remove(x)
```

---

### Two Pointers

#### Trigger Words
1. All The Triplets
1. All The Unique Quadruplets
1. Constant Extra Space
1. Palindrome, Valid Palindrome
1. Array Is Sorted
1. In-Place
1. Pair
1. 

#### Template

**Opposite Direction Template (Sorted Array)**
```python
left, right = 0, len(nums) - 1

while left < right:
    s = nums[left] + nums[right]

    if s == target:
        return [left, right]
    elif s < target:
        left += 1
    else:
        right -= 1
```

**Fast–Slow Pointer Template**
```python
slow = 0

for fast in range(len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]

return slow + 1
```

**Duplicate Skipping Template**
```python
if i > 0 and nums[i] == nums[i-1]:
    continue
```

**Partition Template**
```python
left, right = 0, len(nums) - 1

while left <= right:
    if nums[left] < pivot:
        left += 1
    elif nums[right] > pivot:
        right -= 1
    else:
        nums[left], nums[right] = nums[right], nums[left]
```

---

### Sliding Window

#### Trigger Words
1. Longest / Shortest Substring
1. Sliding Window
1. Size K
1. Subarray Sum, Average
1. Subarray Product
1. Substrings of Size
1. K-Elements, Kth-Length, K-....
1. At Most / At Least / Exactly

#### Template

**Fixed Window Template**
```python
left = 0
window_sum = 0
for right in range(len(nums)):
    window_sum += nums[right]
    if right - left + 1 == k:
        ans = max(ans, window_sum)
        window_sum -= nums[left]
        left += 1
```

**Variable Window Template**
```python
left = 0
window = {}

for right in range(len(s)):
    window[s[right]] = window.get(s[right], 0) + 1

    while condition_is_violated:
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1

    update_answer()
```

**Count-Based Window (Very Common)**
```python
count = 0
for right in range(n):
    if condition:
        count += 1
    
    while count > k:
        if condition:
            count -= 1
        
        left += 1
```

---

### Backtracking

#### Trigger Words
1. Combination Sum
1. Permutations
1. Subsets
1. All Words
1. All Possible Subsets
1. All Possible Unique Permutations
1. All Unique Combinations
1. Multiple Directions
1. All Valid Solutions
1. Decision At Each Step

#### Template

**General Template**
```
result, sol = [], []

backtrack(i):
    Base condition

    # Backtrack
    backtrack(i+1)

    # Picked picked
    Add to sol
    
    # Backtrack
    backtrack(i+1)

    # UNDO
    POP from sol

backtrack(0)
return result
```
> Can Modified According To Problem Description

---

### DFS

#### Trigger Words
1. Maximum Depth
1. Minimum Depth
1. Subtree / 
1. surrounded region
1. minimum / Maximum height
1. Maximum Width
1. length of the longest path

#### Template

**DFS (Iteratively)**
```python
stack = [root]
# Edge case
if root == None:
    return []

result = []

while stack:
curr = stack.pop()
result.append(curr.val)

if curr.right:
    stack.append(curr.right)
if curr.left:
    stack.append(curr.left)


return result
```
> Can Modified According To Problem Description

**DFS (Recursively)**
```python
# Base case
if root == None:
return []

# print(root.val, end=" ")

leftValues = depthFirstSearch(root.left)   # [b,d,e]
rightValues = depthFirstSearch(root.right)  # [c,f]

# For array flattering 
return [root.val, *leftValues, *rightValues]
# return [root.val] + leftValues + rightValues
```
> Can Modified According To Problem Description

---

### BFS

#### Trigger Words
1. Maximum Depth
1. Minimum Depth
1. Level Order Traversal

#### Template

**BFS (Iteratively)**
```python
# Edge case
if root == None:
    return []

queue = [root]

queue = deque(queue)
result = []

while queue:
curr = queue.popleft()
result.append(curr.val)

if curr.left:
    queue.append(curr.left)

if curr.right:
    queue.append(curr.right)


return result
```
> Can Modified According To Problem Description

---

### Binary Search

#### Trigger Words
1. Search
1. Sorted Array
1. O(log n) / O(log(m * n)) runtime complexity
1. sorted in non-decreasing order
1. Find .. in Sorted Array

#### Template

**Binary Search (Basic)**
```python
# Pointers for binary search
left = 0
right = len(nums) - 1

# Runs for last possible element
while left < right:
# Calculate mid
''' mid = (left + right) // 2 '''
mid = left + (right - left) // 2

# If found, return the index
if target == nums[mid]:
    return mid

# If greater, search on right side
elif target > nums[mid]:
    left = mid + 1

# If smaller, search on left side
else:
    right = mid - 1

# If not found, return -1
return -1
```
> Can Modified According To Problem Description

---

### Top K Elements (Heaps)

#### Trigger Words
1. K Frequent Elements
1. K Pairs
1. Top K / Kth Largest / Kth Smallest
1. K Closest
1. Continuous Stream
1. K Sorted Streams

#### Template

**MAX HEAP**
```python
import heapq

# --- Initializing & Building ---
nums = [5, 1, 8, 3, 2]

# Push negated values into min-heap to simulate max-heap
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)

# In-place heapify with negated values -> O(N)
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# --- Common Operations ---
largest = -heapq.heappop(max_heap)      # Extracts max element: 8 (pop -8 -> negate to 8)
peek_largest = -max_heap[0]              # Reads max without removing: 5
```

**MIN HEAP**
```python
import heapq

# --- Initializing & Building ---
heap = []
nums = [5, 1, 8, 3, 2]

# Option A: Push items one by one -> O(N log N)
for num in nums:
    heapq.heappush(heap, num)

# Option B: Convert array to heap in-place -> O(N)
heap = nums[:]
heapq.heapify(heap)

# --- Common Operations ---
smallest = heapq.heappop(heap)          # Extracts min element: 1
peek_smallest = heap[0]                 # Reads min without removing: 2

# Efficient push + pop in one step
val = heapq.heappushpop(heap, 10)       # Pushes 10, then pops & returns min
val = heapq.heapreplace(heap, 12)       # Pops & returns min, then pushes 12
```

---

### Dynamic Programming

#### Trigger Words
1. distinct ways
1. number of possible unique paths
1. Minimum / Maximum cost to reach
1. Longest Common / Longest Increasing
1. Maximum profit with up to K transactions / Cooling period
1. Minimum insertions / deletions to convert X to Y


#### Template

****
```python
# DP table, (n+1)th position holds answer
dp = [0] * (n + 1)

# Set default values
dp[1] = 1

# Looping till n
for i in range(2, n+1):
    # Running sum calculation
    dp[i] = dp[i-1] + dp[i-2]

# Return answer
return dp[n]
```
> Can Modified According To Problem Description