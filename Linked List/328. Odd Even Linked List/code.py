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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


obj = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.oddEvenList(head))            # 1 -> 3 -> 5 -> 2 -> 4


head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)
print(obj.oddEvenList(head))            # 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4