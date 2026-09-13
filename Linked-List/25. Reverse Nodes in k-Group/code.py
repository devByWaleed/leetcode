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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Edge case
        if not head or k == 1:
            return head
        

        # Helper function to reverse k-th group
        def reverse(first, last):
            curr = first
            prev, next_node = None, None

            # curr will handle the traversal
            while curr is not last:
                # Store next node, for tracking rest of list
                next_node = curr.next

                # Reverse the link
                curr.next = prev
                
                # Move prev, points to current node
                prev = curr
                
                # Move curr to continue loop
                curr = next_node

            return prev

        
        counter = 0     # Comparison with k

        first, last = head, head    # For finding k-th group

        # Dummy node for edge cases
        dummy = ListNode(0)
        curr = dummy

        while True:
            counter = 0

            while last and counter != k:
                last = last.next
                counter += 1

            # If got the k-th group, reverse it
            if counter == k:
                prev = reverse(first, last)
                curr.next = prev
                curr = first
                first = last
            else:
                # For lastly nodes
                curr.next = first
                break


        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy, end=" -> ")
            dummy = dummy.next
        '''

        return dummy.next


obj = Solution()


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.reverseKGroup(head, 2))        # 2 -> 1 -> 4 -> 3 -> 5


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(obj.reverseKGroup(head, 3))        # 3 -> 2 -> 1 -> 4 -> 5


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
print(obj.reverseKGroup(head, 2))        # 2 -> 1

# T.C: O(N)
# S.C: O(1)