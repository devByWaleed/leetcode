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
        
        dummy = ListNode(0)

        curr = dummy

        carry = 0       # Carry if sum is >= 10

        while l1 or l2 or carry:
            
            # Step 1.1: Read values from l1 and l2 (0 if list exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Step 1.2: Sum the two digits + carry
            total = val1 + val2 + carry

            # Step 1.3: Determine new digit and new carry
            carry = total // 10
            new_digit = total % 10
            
            # Adding new node with sum value
            curr.next = ListNode(new_digit)

            # Traversing the lists 
            curr = curr.next

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

        return dummy.next


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