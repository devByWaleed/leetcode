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
        # Edge case: head is empty
        if head is None:
            return head
        
        # Pointer for traversal
        curr = head

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

            # For printing whole Linked-List
            '''
            while prev:
                print(prev.val, end=" -> ")
                prev = prev.next
            '''

        # Returning reversed list
        return prev
        

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

# T.C: O(N)     --> Looping through Linked-List
# S.C: O(1)     --> No data structure used