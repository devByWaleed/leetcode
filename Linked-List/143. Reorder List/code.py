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