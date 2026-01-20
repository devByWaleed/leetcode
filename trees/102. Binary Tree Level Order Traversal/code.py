from typing import Optional, List
from collections import deque

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


obj = Solution()

# Test Case
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.levelOrder(root))     # [[3],[9,20],[15,7]]

# Test Case
root = TreeNode(1)
print(obj.levelOrder(root))     # [[1]]

# Test Case
root = None
print(obj.levelOrder(root))     # []