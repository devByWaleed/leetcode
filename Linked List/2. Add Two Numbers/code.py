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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass


obj = Solution()

head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)
print(obj.addTwoNumbers(head1, head2))      # 7 -> 0 -> 8


head1 = ListNode(0)
head1.next = ListNode(None)

head2 = ListNode(0)
head2.next = ListNode(None)
print(obj.addTwoNumbers(head1, head2))      # 0


head1 = ListNode(9)
head1.next = ListNode(9)
head1.next.next = ListNode(9)
head1.next.next.next = ListNode(9)
head1.next.next.next.next = ListNode(9)
head1.next.next.next.next.next = ListNode(9)
head1.next.next.next.next.next.next = ListNode(9)

head2 = ListNode(9)
head2.next = ListNode(9)
head2.next.next = ListNode(9)
head2.next.next.next = ListNode(9)
print(obj.addTwoNumbers(head1, head2))      # 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1