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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


obj = Solution()

# Create linked list: 3 -> 2 -> 0 -> -4
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
# Create cycle: -4 -> 2
head.next.next.next.next = head.next
print(obj.detectCycle(head))        # 2


# Create linked list: 1 -> 2
head = ListNode(1)
head.next = ListNode(2)
# Create cycle: 2 -> 1
head.next.next = head
print(obj.detectCycle(head))        # 1


# Create linked list: 1
head = ListNode(1)
# No cycle
print(obj.detectCycle(head))        # None