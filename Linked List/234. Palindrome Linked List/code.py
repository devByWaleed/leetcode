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
    def isPalindrome(self, head: Optional[ListNode]):

        # Edge case: Only 1 node
        if not head.next:    return True
        

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


        # Comparing both sides
        first, second = head, pre

        while second:

            # If values are different, return False
            if first.val != second.val:    return False

            first = first.next
            second = second.next

        return True     # After looping, return True as list is palindrome


obj = Solution()

# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(obj.isPalindrome(head))        # True


# Create linked list:
head = ListNode(1)
head.next = ListNode(2)
print(obj.isPalindrome(head))        # False

# T.C: O(N)
# S.C: O(1)