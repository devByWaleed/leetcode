from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        # Use pointer for nodes tracking
        curr = root
        
        # Counter for finding kth value
        counter = 0

        # Loop until all nodes are checked
        while stack or curr:
            
            # Checking all left nodes
            while curr:
                stack.append(curr)
                curr = curr.left

            # When reached null, pop and move to
            curr = stack.pop()
            counter += 1

            # Checking kth value
            if counter == k:
                return curr.val
            
            # Move to right side
            curr = curr.right


obj = Solution()


# Test Case
root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.right = TreeNode(2)
print(obj.kthSmallest(root, 1))    # 1


# Test Case
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)
print(obj.kthSmallest(root, 3))    # 3


# Test Case
root = TreeNode(1)

root.right = TreeNode(2)
print(obj.kthSmallest(root, 2))    # 1

# T.C: O(N)
# S.C: O(N)


# Works on strictly left tree
'''
stack = [root]

# Adding all left nodes to stack
while True:
    curr = stack[-1]
    if curr.left:
        stack.append(curr.left)
    else:
        # Loop stops when tree ends
        break

# Store kth smallest value
kth_val = 0

# Looping k times to get targeted value
for _ in range(k):
    kth_val = stack.pop()

return kth_val.val
'''