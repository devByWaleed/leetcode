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
        # Starting with root
        lca = [root]

        def search(root):
            # Base case
            if not root:
                return
            
            # update the value for each sub-tree
            lca[0] = root

            # If we found p, q as root, return nothing
            if root is p or root is q:
                return
            
            # If value is less, search on right side
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            
            # If value is greater, search on left side
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            
            # If not found, return nothing
            else:
                return
            
        # Pass to helper function
        search(root)

        # Return the node
        return lca[0]


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

# T.C: O(LOG(N))
# S.C: O(1)