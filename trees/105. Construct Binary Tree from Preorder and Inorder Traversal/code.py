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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Edge case
        if not preorder or not inorder:
            return None
        
        # Creating root node
        root = TreeNode(preorder[0])

        # Finding index of root node inside inorder
        mid = inorder.index(preorder[0])

        # Get left child & add it recursively
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        
        # Get right child & add it recursively
        root.right = self.buildTree(preorder[mid+1: ], inorder[mid+1: ])

        # Printing Tree in BFS form
        '''
        print(breathFirstSearch(root))
        '''

        # Return root as newly constructed tree
        return root


def breathFirstSearch(root: Optional[TreeNode]):
    if not root:
        return []
    
    # Using deque for efficient pops from the left
    queue = deque([root])
    result = []

    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        current_level_vals = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level_vals.append(node.val)
            
            # Add children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Append the entire level to results
        result.append(current_level_vals)

    return result


obj = Solution()

# Test Case
pre_order = [3, 9, 20, 15, 7]
in_order = [9, 3, 15, 20, 7]

print(obj.buildTree(pre_order, in_order))   # 3

# Test Case
pre_order = [-1]
in_order = [-1]

print(obj.buildTree(pre_order, in_order))   # -1

# T.C: O(N)
# S.C: O(N)