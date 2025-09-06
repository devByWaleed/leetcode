from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass

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