# Blind 75 Part 2: Linked List

This part contains problems related to `Linked-List`

`Total Count = 6`

---

## 1. LeetCode 141: Linked Lsit Cycle (Easy)

* **Identified Pattern Upfront:** Linked-List / Two-Pointers / Slow-Fast Pointers
* **Time Taken:** 2 minutes
* **Solution Folder:** [`../../Linked-List/141.%20Linked%20List%20Cycle/`](../../Linked-List/141.%20Linked%20List%20Cycle/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/linked-list-cycle/submissions/2140249505)

### Code Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge casee: 1 node
        if not head or not head.next:
            return False

        # Initialize slow & fast pointers
        slow = head
        fast = head

        # Looping till end of list
        while fast and fast.next:
            # 1 time movement
            slow = slow.next

            # 2 time movement
            fast = fast.next.next

            # Checking for same position: cycle found
            if slow == fast:
                return True

        # No cycle found
        return False

        
obj = Solution()

# Create linked list:
head = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node_4 = ListNode(-4)

head.next = node2
node2.next = node0
node0.next = node_4
node_4.next = node2   # cycle created here
print(obj.hasCycle(head))       # True


# Create linked list:
head = ListNode(1)
node2 = ListNode(2)

head.next = node2
node2.next = head   # cycle created here
print(obj.hasCycle(head))       # True


# Create linked list:
head = ListNode(1)  # No cycle created
print(obj.hasCycle(head))       # False

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used
```

---

## 2. LeetCode 206: Reverse Linked List (Easy)

* **Identified Pattern Upfront:** Linked-List / Pointers
* **Time Taken:** 16 minutes
* **Solution Folder:** [`../../Linked-List/206.%20Reverse%20Linked%20List/`](../../Linked-List/206.%20Reverse%20Linked%20List/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/reverse-linked-list/submissions/2140271661)

### Code Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: head is empty
        if head is None:
            return head
        
        # Pointer for traversal
        curr = head

        # Pointers for next node + reversed list tracking
        next_p, prev = None, None

        # Looping till end of list
        while curr:
            # Save next number reference
            next_p = curr.next

            # Break the link of "curr"
            curr.next = prev

            # Adding "curr" into "prev" pointer, making the reversed list
            prev = curr

            # Move curr with saved reference for list traversal
            curr = next_p

            # For printing whole Linked-List
            '''
            while prev:
                print(prev.val, end=" -> ")
                prev = prev.next
            '''

        # Returning reversed list
        return prev
        

obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.reverseList(head))        # 5 -> 4 -> 3 -> 2 -> 1


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
print(obj.reverseList(head))        # 2 -> 1


# Create linked list:
head = None
print(obj.reverseList(head))        # None

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used
```

---

## 3. LeetCode 21: Merge Two Sorted List (Easy)

* **Identified Pattern Upfront:** Linked-Lsit / Pointers
* **Time Taken:** 18 minutes
* **Solution Folder:** [`../../Linked-List/21.%20Merge%20Two%20Sorted%20Lists/`](../../Linked-List/21.%20Merge%20Two%20Sorted%20Lists/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/merge-two-sorted-lists/submissions/2140303503)

### Code Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Pointers for both lists
        curr_l1 = list1
        curr_l2 = list2

        # Dummy node & it's pointer
        dummy = ListNode(0)
        curr_dummy = dummy

        while curr_l1 and curr_l2:
            # Add value of list1
            if curr_l1.val <= curr_l2.val:
                curr_dummy.next = curr_l1
                curr_l1 = curr_l1.next
            # Add value of list2
            else:
                curr_dummy.next = curr_l2
                curr_l2 = curr_l2.next

            # Move pointer of dummy list
            curr_dummy = curr_dummy.next

        # If 1 list becomes empty, add other
        if not curr_l1:     curr_dummy.next = curr_l2
        if not curr_l2:     curr_dummy.next = curr_l1

        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy.val, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next

        
obj = Solution()

# Create linked list:
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(obj.mergeTwoLists(list1, list2))      # 1 -> 1 -> 2 -> 3 -> 4 -> 4


# Create linked list:
list1 = None

list2 = None
print(obj.mergeTwoLists(list1, list2))      # None


# Create linked list:
list1 = None

list2 = ListNode(0)
list2.next = None
print(obj.mergeTwoLists(list1, list2))      # 0

# T.C: O(N + M)     --> Looping through both Linked-List
# S.C: O(1)         --> No data structure used
```















---

## 1. LeetCode No.: Name (Difficulty)

* **Identified Pattern Upfront:** 
* **Time Taken:**  minutes
* **Solution Folder:** [`../../`](../../)
* **Submittion Link:** [`Link`]()

### Code Solution

```python
```