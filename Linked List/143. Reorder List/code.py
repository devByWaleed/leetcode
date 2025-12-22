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
    # def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Initialize two pointers to find the middle of the linked list
        slow, fast = head, head

        # Move slow by 1 step and fast by 2 steps to locate the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Start reversing the second half of the list
        curr = slow.next        # Head of second half
        slow.next = None        # Split the list into two halves
        prev = None             # Will become new head of reversed half

        # Reverse the second half using three-pointer technique
        while curr:

            next_node = curr.next   # Store next node
            curr.next = prev        # Reverse current node's pointer
            prev = curr             # Move prev forward
            curr = next_node        # Move curr forward


        # Merge the first half and the reversed second half alternately
        first, second = head, prev

        while second:

            temp1 = first.next      # Store next node of first half
            temp2 = second.next     # Store next node of second half

            first.next = second     # Link first node to second
            second.next = temp1     # Link second node back to first half

            first = temp1           # Move first pointer forward
            second = temp2          # Move second pointer forward

        
        # For printing whole Linked-List
        '''
        while head:
            print(head, end=" -> ")
            head = head.next
        '''

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

# T.C: O(N)
# S.C: O(1)