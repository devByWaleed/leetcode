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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Pointer for traversing tree
        curr = root

        while curr:
            # If smaller, lies on left side
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # If larger, lies on right side
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Current is the ancestor
            else:
                return curr


obj = Solution()


# Test Case
root = TreeNode(6)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p_node = root.left        # This is the node with value 2
q_node = root.right       # This is the node with value 8
print(obj.lowestCommonAncestor(root, p_node, q_node))    # 6


# Test Case
root = TreeNode(6)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p_node = root.left             # This is the node with value 2
q_node = root.left.right       # This is the node with value 4
print(obj.lowestCommonAncestor(root, p_node, q_node))    # 2


# Test Case
root = TreeNode(2)

root.left = TreeNode(1)

p_node = root            # This is the node with value 2
q_node = root.left       # This is the node with value 1
print(obj.lowestCommonAncestor(root, p_node, q_node))    # 2

# T.C: O(H)     --> Traversing tree to height H
# S.C: O(1)     --> No data structure used