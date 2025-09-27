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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finding mid
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse 2nd half
        pre, temp = None, None
        
        curr = slow     # We need to reverse 2nd half part

        while curr:
            temp = curr.next    # temp points to next element

            curr.next = pre     # pre value set to next pointer of current

            pre = curr          # pre set to current value

            curr = temp         # current pointer set to temp(next element)

        # Saving both sides
        first, second = head, pre

        # Condition for all nodes in the list
        while second and second.next:

            # Saving next pointers
            temp1 = first.next
            temp2 = second.next

            # Alternating the nodes
            first.next = second
            second.next = temp1

            # Save next pointers for alternating
            first = temp1
            second = temp2


        # For printing whole Linked-List
        '''
        while head:
            print(head.val, end=" -> ")
            head = head.next
        '''


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