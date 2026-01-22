from typing import Optional, List

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


obj = Solution()

# Test Case
pre_order = [3, 9, 20, 15, 7]
in_order = [9, 3, 15, 20, 7]

print(obj.buildTree(pre_order, in_order))   # 3

# Test Case
pre_order = [-1]
in_order = [-1]

print(obj.buildTree(pre_order, in_order))   # -1