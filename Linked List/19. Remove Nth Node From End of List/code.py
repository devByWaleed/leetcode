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
        pass


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