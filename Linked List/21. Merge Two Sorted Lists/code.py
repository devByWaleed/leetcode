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
        pass


obj = Solution()

# Create linked list:
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

print(obj.mergeTwoLists(head1, head2))      # 1 -> 1 -> 2 -> 3 -> 4 -> 4


# Create linked list:
head1 = None

head2 = None
print(obj.mergeTwoLists(head1, head2))      # None


# Create linked list:
head1 = None

head2 = ListNode(0)
head2.next = None
print(obj.mergeTwoLists(head1, head2))      # 0