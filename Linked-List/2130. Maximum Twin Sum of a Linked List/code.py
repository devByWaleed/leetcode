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
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Dummy node for edge cases
        dummy = ListNode(0)
        dummy.next = head

        max_sum = 0     # Keep final answer


        # Initialize two pointers to find the middle of the linked list
        slow, fast = dummy, dummy


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

        # Re-link both parts
        slow.next = prev

        # Looping and finding maximum sum
        while prev:
            current_sum = head.val + prev.val
            max_sum = max(max_sum, current_sum)

            head = head.next
            prev = prev.next

                
        # For printing whole Linked-List
        '''
        while dummy:
            print(dummy, end=" -> ")
            dummy = dummy.next
        '''
        return max_sum


obj = Solution()


# Create linked list:
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(obj.pairSum(head))      # 6


# Create linked list:
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

print(obj.pairSum(head))      # 7


# Create linked list:
head = ListNode(1)
head.next = ListNode(100000)

print(obj.pairSum(head))      # 100001

# T.C: O(N)
# S.C: O(1)