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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Used list bcz it will change the value
        rather than creating a new variable inside recursive function
        ''' 
        max_sum = [root.val]

        def dfs(root):
            # Base case
            if not root:
                return 0
            
            # Handling left & right childs
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            # Handling -ve values
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            # Calculate max path sum with SPLIT
            max_sum[0] = max(max_sum[0], root.val + max_left + max_right)

            # Returning sum of valid path by picking either left or right
            return root.val + max(max_left, max_right)
        
        
        # Calling function for calculation
        dfs(root)

        return max_sum[0]       # Returning max sum


obj = Solution()


# Test Case
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
print(obj.maxPathSum(root))    # 6


# Test Case
root = TreeNode(-10)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.maxPathSum(root))    # 42

# T.C: O(N)
# S.C: O(H)