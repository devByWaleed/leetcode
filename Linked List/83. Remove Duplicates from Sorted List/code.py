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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Using current pointer
        current = head

        # Looping untill current and next node will be Null
        while current != None and current.next != None:

            # Checking for duplicates
            if current.val == current.next.val:

                # Moving our next pointer to skip duplicated one
                current.next = current.next.next

            # If no duplicates, then traverse through the list
            else:
                current = current.next

        # For printing whole Linked-List
        '''
        while head:
            print(head.val, end=" -> ")
            head = head.next
        '''

        return head


obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
# Reverse it
print(obj.deleteDuplicates(head))        # 1 -> 2


# Create linked list:
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
# Reverse it
print(obj.deleteDuplicates(head))        # 1 -> 2 -> 3

# T.C: O(N)
# S.C: O(1)