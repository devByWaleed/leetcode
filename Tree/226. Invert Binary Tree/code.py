from typing import Optional
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base cases
        if root == None:
            return None
        if not root.left and not root.right:
            return root
        
        # Inverting child nodes
        root.left, root.right = root.right, root.left

        # Inverting sub-childs with recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Printing Tree in BFS form
        '''
        print(breathFirstSearch(root))
        '''
        return root


'''
def breathFirstSearch(root):
  # Edge case
  if root == None:
     return []
  
  queue = [root]

  queue = deque(queue)
  result = []

  while queue:
    curr = queue.popleft()
    result.append(curr.val)
    
    if curr.left:
      queue.append(curr.left)

    if curr.right:
      queue.append(curr.right)


  return result
'''

obj = Solution()

# Test Case
root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(obj.invertTree(root))     # 4

# Test Case
root = TreeNode(2)

root.left = TreeNode(1)
root.right = TreeNode(3)
print(obj.invertTree(root))     # 2

# Test Case
root = None
print(obj.invertTree(root))     # None

# T.C: O(N)
# S.C: O(H)  H = height of tree