from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Edge case
        if not head:
            return head
        
        # Hashmap to create deep copy
        hash_map = {}

        # Traversing and creating new nodes with same values
        pointer = head
        while pointer:
            hash_map[pointer] = Node(pointer.val)
            pointer = pointer.next

        
        # Traversing and linking next & random pointers using original list
        curr = head
        while curr:
            copy_node = hash_map[curr]
            copy_node.next = hash_map.get(curr.next)
            copy_node.random = hash_map.get(curr.random)
            curr = curr.next

        
        # For printing whole Linked-List
        '''
        for val, random in hash_map.items():
            print(f"{val} ➤ {random}", end=" ---> ")
        '''

        # New list head
        return hash_map[head]
        

obj = Solution()

# Create linked list:
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

head.random = None
head.next.random = head                # 13 -> 7
head.next.next.random = head.next.next.next.next  # 11 -> 1
head.next.next.next.random = head.next.next       # 10 -> 11
head.next.next.next.next.random = head             # 1 -> 7

print(obj.copyRandomList(head))         # 7 ➤ 7 ---> 13 ➤ 13 ---> 11 ➤ 11 ---> 10 ➤ 10 ---> 1 ➤ 1


# Create linked list:
head = Node(1)
head.next = Node(2)

head.random = head.next     # 1 -> 2
head.next.random = head.next # 2 -> 2

print(obj.copyRandomList(head))         # 1 ➤ 1 ---> 2 ➤ 2


# Create linked list:
head = Node(3)
head.next = Node(3)
head.next.next = Node(3)

# Assign random pointers
head.random = None
head.next.random = head        # second node -> first node
head.next.next.random = None

print(obj.copyRandomList(head))         # 3 ➤ 3 ---> 3 ➤ 3 ---> 3 ➤ 3

# T.C: O(N)
# S.C: O(N)