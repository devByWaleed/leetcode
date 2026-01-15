# Linked List
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None


    def get(self, index: int):
        current = self.head
        current_index = 0       # To check the value of given index by comparison
        while current:
            if current_index == index:
                return current.val
            current = current.next
            current_index += 1
        return -1

    def addAtHead(self, val):
        current = Node(val)    # creating new node
        current.next = self.head
        # current = self.head       # Incorrect assigning
        self.head = current
        
    def addAtIndex(self, index: int, val: int):
        if index < 0:
            return "Index out of bound"
        
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
            
        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1
        
        if not current:
            # print("Index is out of bounds.")
            return "Index is out of bounds."
        
        new_node.next = current.next
        current.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)    # creating new node

        if not self.head:       # if list is empty, then head(1st element) will be new_node
            self.head = new_node

        else:                   # we specify head to current and it checks the space, then it add new node to the last                   
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        

    def deleteAtIndex(self, index: int):
        if not self.head:       # if list is empty, then head(1st element) will be new_node
            return "List is Empty"
        
        if index == 0:
            self.head = self.head.next

        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1
        
        if not current or not current.next:
            return "Index is out of bounds."
        
        current.next = current.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
print(obj.get(1))       # 2
obj.deleteAtIndex(1)
print(obj.get(1))       # 3

'''
None
None
None
None
2
None
3
'''

# T.C: O(N)
# S.C: O(N)