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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function to validate BST
        def validate(node, low=-float("inf"), high=float("inf")):
            # Edge case
            if not node:
                return True
            
            # BST condition
            if not (low < node.val < high):
                return False
            
            # Recursive call on left & right child
            left_BST = validate(node.left, low, node.val)
            right_BST = validate(node.right, node.val, high)
            
            # Return the answer
            return (left_BST and right_BST)
        
        return validate(root)
    

obj = Solution()

# Test Case
root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
print(obj.isValidBST(root))    # True

# Test Case
root = TreeNode(5)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(obj.isValidBST(root))    # False

# Test Case
root = TreeNode(1)

root.left = TreeNode(1)
print(obj.isValidBST(root))    # True

# T.C: O(N)
# S.C: O(N)


# Logical Issues
'''
# Edge case
        if not root.left and not root.right:
            return True
        
        
        # Checking root for BST
        rootBST = [(root.left.val < root.val and root.right.val > root.val)]
        
        # Base case for recursive call
        if rootBST[0]:
            return True
        
        # Checking left & right childs for BST
        leftBST = self.isValidBST(root.left)
        rightBST = self.isValidBST(root.right)
        
        # Answer based on all 3 conditions
        return rootBST[0] and leftBST and rightBST

'''