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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pass


obj = Solution()

# ------------------ Test-case 1 ------------------
# Shared part (intersection)
intersect = ListNode(8)
intersect.next = ListNode(4)
intersect.next.next = ListNode(5)

# List A: 4 -> 1 -> [8 -> 4 -> 5]
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersect

# List B: 5 -> 6 -> 1 -> [8 -> 4 -> 5]
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersect
print(obj.getIntersectionNode(headA, headB))        # 8


# ------------------ Test-case 2 ------------------
# Shared part (intersection)
intersect = ListNode(2)
intersect.next = ListNode(4)

# List A: 1 -> 9 -> 1 -> [2 -> 4]
headA = ListNode(1)
headA.next = ListNode(9)
headA.next.next = ListNode(1)
headA.next.next.next = intersect

# List B: 3 -> [2 -> 4]
headB = ListNode(3)
headB.next = intersect
print(obj.getIntersectionNode(headA, headB))        # 2


# ------------------ Test-case 3 ------------------
# List A: 2 -> 6 -> 4
headA = ListNode(2)
headA.next = ListNode(6)
headA.next.next = ListNode(4)

# List B: 1 -> 5
headB = ListNode(1)
headB.next = ListNode(5)

# No intersection (different node references)
print(obj.getIntersectionNode(headA, headB))        # None