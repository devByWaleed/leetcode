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
        # Edge case
        if not head or not head.next:
            return False
        
        # Initialize 2 pointers at head
        slow, fast = head, head

        # Condition for looping till end of list
        while fast and fast.next:

            # Moving slow pointer 1 time
            slow = slow.next

            # Moving slow pointer 2 time
            fast = fast.next.next

            # If pointers meet, cycle detected. Otherwise no cycle
            if slow == fast:
                return True
            
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

# T.C: O(N)
# S.C: O(1)