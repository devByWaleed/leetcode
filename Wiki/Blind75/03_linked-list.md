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

## 4. LeetCode 19: Remove Nth Node From End of List (Medium)

* **Identified Pattern Upfront:** Linked List / Slow-Fast Pointers
* **Time Taken:** 44 minutes
* **Solution Folder:** [`../../Linked-List/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/`](../../Linked-List/19.%20Remove%20Nth%20Node%20From%20End%20of%20List/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/2141261221)

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:       
        # Dummy node for easy head removal
        dummy = ListNode(0)
        dummy.next = head

        # Both pointers at dummy
        slow, fast = dummy, dummy

        # Including n
        for _ in range(n+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Removing Nth node
        slow.next = slow.next.next


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy.val, end=" -> ")
            dummy = dummy.next
        '''
        return dummy.next


obj = Solution()

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.removeNthFromEnd(head, 2))        # 1 -> 2 -> 3 -> 5


# Create linked list: 1
head = ListNode(1)
print(obj.removeNthFromEnd(head, 1))        # None


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
print(obj.removeNthFromEnd(head, 1))        # 1


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
print(obj.removeNthFromEnd(head, 2))        # 2

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used
```

---

## 5. LeetCode 23: Merge k Sorted Lists (Hard)

* **Identified Pattern Upfront:** linked-List / Min-Heap
* **Time Taken:** 7 minutes
* **Solution Folder:** [`../../Linked-List/23.%20Merge%20k%20Sorted%20Lists/`](../../Linked-List/23.%20Merge%20k%20Sorted%20Lists/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/merge-k-sorted-lists/submissions/2141301247)

### Code Solution

```python
from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Dummy node for edge cases
        dummy = ListNode(0)
        curr = dummy
        
        # Add numbers into Min-Heap
        for i in range(len(lists)):
            if lists[i]:
                # Pattern: val, index, node
                heapq.heappush(heap, (lists[i].val, i, lists[i]))


        # Merging k sorted lists
        while heap:
            # POP the node with smallest value
            num, index, node = heapq.heappop(heap)

            # Adding node and moving to .next
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next
        

obj = Solution()

# Create linked list:
# List 1: 1 -> 4 -> 5
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

# List 2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# List 3: 2 -> 6
list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1, list2, list3]

print(obj.mergeKLists(lists))       # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6


# Create linked list:
lists = []

print(obj.mergeKLists(lists))       # None


# Create linked list:
lists = [None]

print(obj.mergeKLists(lists))       # None

# T.C: O(N LOG K)       --> N heap operations and k elements adding to Min-Heap
# S.C: O(K)             --> Min-Heap used, store K elements


'''
# Print lists column wise
while any(lists):                     # continue while at least one list is not None
    for j in range(len(lists)):
        if lists[j]:                  # if current list still has nodes
            print(lists[j].val, end=" -> ")
            lists[j] = lists[j].next  # move down in that list
'''
```

---

## 6. LeetCode 143: Reorder List (Medium)

* **Identified Pattern Upfront:** Linked-List / Slow-Fast Pointers
* **Time Taken:** 25 minutes
* **Solution Folder:** [`../../Linked-List/143.%20Reorder%20List/`](../../Linked-List/143.%20Reorder%20List/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/reorder-list/submissions/2141329888)

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
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # 2. Reversing 2nd half
        curr = second
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

        # 3. Merging
        first = head
        second = prev

        while second:
            # Saving .next reference
            temp1 = first.next
            temp2 = second.next

            # Re-link the pattern
            first.next = second
            second.next = temp1

            # Moving forward
            first = temp1
            second = temp2

        # For printing whole Linked-List
        '''
        while head:
            print(head.val, end=" -> ")
            head = head.next
        '''

        # Returning merged list
        # return head

        
obj = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(obj.reorderList(head))        # 1 -> 4 -> 2 -> 3


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.reorderList(head))        # 1 -> 5 -> 2 -> 4 -> 3

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used
```