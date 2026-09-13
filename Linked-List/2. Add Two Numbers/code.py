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

        dummy = ListNode(0)     # Dummy node for new merged list
        curr = dummy        # For traversing in dummy

        carry = 0       # For storing carry for sum >= 10

        # Loop until we have values / carry
        while l1 or l2 or carry:

            # If no value, add 0 as edge case
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            # Extract carry & digit despite the sum
            carry = total // 10
            digit = total % 10

            # Add to dummy and mov curr
            curr.next = ListNode(digit)
            curr = curr.next

            # Also works
            '''
            # If sum >= 10, extract digit and add to dummy
            if total >= 10:
                carry = total // 10
                digit = total % 10

                curr.next = ListNode(digit)
                curr = curr.next
            
            # Else add whole total and reset carry
            else:
                curr.next = ListNode(total)
                curr = curr.next
                carry = 0
            '''
            

            # Update the head if has values
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        
        # For printing whole Linked-List
        '''
        while dummy.next:
            print(dummy.next, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next   # return new head
    

obj = Solution()

head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)
print(obj.addTwoNumbers(head1, head2))      # 7 -> 0 -> 8


head1 = ListNode(0)

head2 = ListNode(0)
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

# T.C: O(Max(M,N))
# S.C: O(Max(M,N))