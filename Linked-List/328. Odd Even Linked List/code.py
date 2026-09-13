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

        # Edge case
        if not head or not head.next:
            return head
        
        # Odd is traversing pointer, 
        odd, even = head, head.next
        
        # even_head is even list reference
        even_head = even

        
        while even and even.next:
            odd.next = even.next    # Assigning next value
            odd = odd.next      # Traversing
            even.next = odd.next    # Assigning next value
            even = even.next        # Traversing

        # After loop, add even_head if remain
        odd.next = even_head

        # For printing whole Linked-List
        '''
        while head:
            print(head, end=" -> ")
            head = head.next
        '''

        return head


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

# T.C: O(N)
# S.C: O(1)