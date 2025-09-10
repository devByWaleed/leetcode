from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Edge case
        if not head:
            return head
        

        # Pointer for holding reverse list
        temp = None

        # Store the next node for not losing reference
        next_node = head.next
    
        # Traversing from head
        while head:

            # Reversing current node's pointer
            head.next = temp

            # Assigning current element to reversed list
            temp = head

            # Advance the head to the next node in the original list
            head = next_node

            # Update next node if exists (for traversing)
            if next_node:
                next_node = next_node.next

        # For printing whole Linked-List
        '''
        while temp:
            print(temp, end=" -> ")
            temp = temp.next
        '''
        
        # Returning the reversed linked list
        return temp

        
obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.reverseList(head))        # 5 -> 4 -> 3 -> 2 -> 1


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
print(obj.reverseList(head))        # 2 -> 1


# Create linked list:
head = None
print(obj.reverseList(head))        # None

# T.C: O(N)
# S.C: O(1)