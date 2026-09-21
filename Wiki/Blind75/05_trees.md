# Blind 75 Part 5: Trees

This part contains problems related to `Trees`, `DFS`, `BFS`, `Tries`

`Total Count = 14`

---

## 1. LeetCode 104: Maximum Depth of Binary Tree (Easy)

* **Identified Pattern Upfront:** Tree / DFS / BFS
* **Time Taken:** 28 minutes
* **Solution Folder:** [`../../Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree/`](../../Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/2143403105)

### Code Solution

```python
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: Empty Tree
        if root == None:
            return 0

        # Creating deque for constant node removal
        queue = deque([ root ])

        # Final depth count
        depth = 0

        while queue:
            # Get size of current level
            level = len(queue)

            for _ in range(level):
                # POP current node
                curr = queue.popleft()

                # Add left & right childs
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            # After processing level
            depth += 1

        return depth

        
obj = Solution()

# Test Case
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.maxDepth(root))     # 3

# Test Case
root = TreeNode(1)

root.right = TreeNode(2)
print(obj.maxDepth(root))     # 2

# T.C: O(N)     --> Looping through N nodes
# S.C: O(W)     --> Queue used for W width tree
```

---

## 2. LeetCode 102: Binary Tree Level Order Traversal (Medium)

* **Identified Pattern Upfront:** Tree / BFS
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../Tree/102.%20Binary%20Tree%20Level%20Order%20Traversal/`](../../Tree/102.%20Binary%20Tree%20Level%20Order%20Traversal/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/2144421763)

### Code Solution

```python
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
        # Final answer
        result = []
        # Queue for BFS
        queue = deque([ root ])
        
        while queue:
        # Get length for completing level traversal
            level = len(queue)
            level_nodes = []
            
            for _ in range(level):
                curr = queue.popleft()
                # Add current value
                level_nodes.append(curr.val)

                # Add left & right childs to queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    # Add level's array to result
            result.append(level_nodes)
    
        return result
   
        
obj = Solution()

# Test Case
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.levelOrder(root))     # [[3], [9,20], [15,7]]

# Test Case
root = TreeNode(1)
print(obj.levelOrder(root))     # [[1]]

# Test Case
root = None
print(obj.levelOrder(root))     # []

# T.C: O(N)     --> Looping through the queue
# S.C: O(N)     --> Array used for N nodes
```

---

## 3. LeetCode 124: Binary Tree Maximum Path Sum (Hard)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 15 minutes
* **Solution Folder:** [`../../Tree/124.%20Binary%20Tree%20Maximum%20Path%20Sum/`](../../Tree/124.%20Binary%20Tree%20Maximum%20Path%20Sum/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/2145415922)

### Code Solution

```python
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
            # Edge case: Empty Tree
            if not root:
                return 0
            
            # Handle left & right childs
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            
            # Handle -ve value
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)
            
            # Store max sum
            max_sum[0] = max(max_sum[0], root.val+max_left+max_right)

            # Return sum of root with either left OR right
            return root.val + max(max_left, max_right)
        
        # Call function
        dfs(root)
        
        # Return Max Path Sum
        return max_sum[0]


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

# T.C: O(N)     --> Function call on N nodes
# S.C: O(H)     --> Recursive call-stack of height H tree
```

---

## 4. LeetCode 226: Invert Binary Tree (Easy)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 10 minutes
* **Solution Folder:** [`../../Tree/226.%20Invert%20Binary%20Tree/`](../../Tree/226.%20Invert%20Binary%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/invert-binary-tree/submissions/2144511668)

### Code Solution

```python
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
        # Edge cases: Empty Tree & Only Root
        if not root:
            return None
        
        
        def dfs(node):
            # Base condition: Node is empty
            if not node:
                return None
                
            # Inverting
            node.left, node.right = node.right, node.left
            
            # Passing left child
            dfs(node.left)
            # Passing right child
            dfs(node.right)
        
        
        # Passing give root
        dfs(root)
        
        # Printing Tree in BFS form
        '''
        print(breathFirstSearch(root))
        '''
        
        # Returning
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

# Test Case
root = 1

#root.left = None
root.right = 2
print(obj.invertTree(root))

# T.C: O(N)     --> Function call on N nodes
# S.C: O(H)     --> Recursive call-stack of height H tree
```

---

## 5. LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal (Medium)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 26 minutes
* **Solution Folder:** [`../../Tree/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/`](../../Tree/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/2145404783)

### Code Solution

```python
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
        
        # Create root node
        root = TreeNode(preorder[0])

        # Find index of current number in inorder array
        mid = inorder.index(preorder[0])

        # Attaching left & right child recursively
        root.left = self.buildTree(preorder[1 : mid+1], inorder[: mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Printing Tree in BFS form
        '''
        # print(breathFirstSearch(root))
        '''

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

# T.C: O(N)     --> Working on N numbers array
# S.C: O(N)     --> Recursive call-stack of N size used
```

---

## 6. LeetCode 98: Validate Binary Search Tree (Medium)

* **Identified Pattern Upfront:** Tree / DFS
* **Time Taken:** 21 minutes
* **Solution Folder:** [`../../Tree/98.%20Validate%20Binary%20Search%20Tree/`](../../Tree/98.%20Validate%20Binary%20Search%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/validate-binary-search-tree/submissions/2145466108)

### Code Solution

```python
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

        def validate(node, low = -float("inf"), high = float("inf")):
            # Edge case
            if not node:
                return True

            # Checking for value
            if not (low < node.val < high):
                return False

            # Validate it's left BST
            left_bst = validate(node.left, low, node.val)

            # Validate it's right BST
            right_bst = validate(node.right, node.val, high)

            # Final validation
            return left_bst and right_bst

        # Return answer
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

# T.C: O(N)     --> Working on N nodes
# S.C: O(N)     --> Recursive call-stack of N size used
```

---

## 7. LeetCode 230: Kth Smallest Element in a BST (Medium)

* **Identified Pattern Upfront:** Tree / BST / DFS / Stack
* **Time Taken:** 17 minutes
* **Solution Folder:** [`../../Tree/230.%20Kth%20Smallest%20Element%20in%20a%20BST/`](../../Tree/230.%20Kth%20Smallest%20Element%20in%20a%20BST/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/2145501493)

### Code Solution

```python
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
        # Stack for DFS traversal
        stack = []

        # Pointer for root
        curr = root

        # Counter for checking kth value
        counter = 0

        # While traversing BST and getting root
        while stack or curr:

            while curr:
                # Add to stack and move to left childs
                stack.append(curr)
                curr = curr.left

            # Popping and incrementing counter for k values checking
            curr = stack.pop()
            counter += 1

            # If kth smallest found, return it's .val
            if counter == k:
                return curr.val

            # Move to right side of BST
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

# T.C: O(H + k)     --> Traversing through H nodes + k lookup
# S.C: O(H)         --> Stack used for h height BST
```

---

## 8. LeetCode 235: Lowest Common Ancestor of a Binary Search Tree (Medium)

* **Identified Pattern Upfront:** Tree / BST / DFS
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../Tree/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/`](../../Tree/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/2146363869)

### Code Solution

```python
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
```

---

## 9. LeetCode 100: Same Tree (Easy)

* **Identified Pattern Upfront:** Tree / BFS / DFS
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../Tree/100.%20Same%20Tree/)`](../../Tree/100.%20Same%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/same-tree/submissions/2146388097)

### Code Solution

```python
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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Edge cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # Save root in pair
        queue = deque([ (p, q) ])

        while queue:
            # Pop the leftmost
            node1, node2 = queue.popleft()

            # If both empty, continue
            if not node1 and not node2:
                continue

            # 1 is empty or value not matched
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # Add left & right childs
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
            

        return True


obj = Solution()


# Test Case 1
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(obj.isSameTree(p, q))    # True


# Test Case 2
p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(obj.isSameTree(p, q))    # False


# Test Case 3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)

q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)

print(obj.isSameTree(p, q))    # False

# T.C: O(N)     --> Traversing through every node in the smaller tree once
# S.C: O(H)     --> Call-Stack used for H height tree
```

---

## 10. LeetCode 572: Subtree of Another Tree Name (Easy)

* **Identified Pattern Upfront:** Tree / BFS / DFS
* **Time Taken:** 20 minutes
* **Solution Folder:** [`../../Tree/572.%20Subtree%20of%20Another%20Tree/`](../../Tree/572.%20Subtree%20of%20Another%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/subtree-of-another-tree/submissions/2146409452)

### Code Solution

```python
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
    def isSubtree(self, root: Optional['TreeNode'], subRoot: Optional['TreeNode']) -> bool:
        # Function to check sub_tree
        def isSameTree(p, q):
            queue = deque([ (p, q) ])

            while queue:
                # Pop the leftmost
                node1, node2 = queue.popleft()

                # If both empty, continue
                if not node1 and not node2:
                    continue

                # 1 is empty or value not matched
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                # Add left & right childs
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

            return True


        # Working on "root"
        main_queue = deque([ root ])

        while main_queue:
            curr = main_queue.popleft()

            if curr.val == subRoot.val:
                if isSameTree(curr, subRoot):
                    return True
                
            if curr.left:
                main_queue.append(curr.left)
            if curr.right:
                main_queue.append(curr.right)
        
        return False


obj = Solution()


# Test Case 1
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(obj.isSubtree(root, subRoot))    # True


# Test Case 2
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(obj.isSubtree(root, subRoot))    # False

# T.C: O(M * N)     --> N = nodes in root, M = nodes in subRoot (isSame check at each node)
# S.C: O(max(M,N))         --> Recursion stack, H = height of the root tree
```

---

## 11. LeetCode 297: Serialize and Deserialize Binary Tree (Hard)

* **Identified Pattern Upfront:** DFS / Binary Tree
* **Time Taken:** 42 minutes
* **Solution Folder:** [`../../Design/297.%20Serialize%20and%20Deserialize%20Binary%20Tree/`](../../Design/297.%20Serialize%20and%20Deserialize%20Binary%20Tree/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/2147416034)

### Code Solution

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # Customize this to show node value during de-bugging
    def __repr__(self): 
        return f"{self.val}"

        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            # for empty area
            if not node:    return ["N"]

            # Concatenation of all sub-arrays
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        # Joining to create string
        serialized = ",".join(dfs(root))

        return serialized
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # Splitting the string to form arary
        data = data.split(",")

        # Create iterable object
        vals = iter(data)

        def dfs():
            # Get next element
            val = next(vals)

            # Empty node:
            if val == "N":  return None

            # Creating node
            node = TreeNode(int(val))

            # Creating left and right childs
            node.left = dfs()
            node.right = dfs()

            # Returning root node
            return node
        
        return dfs()


# Your Codec object will be instantiated and called as such:

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Driver Execution
ser = Codec()
deser = Codec()

serialized_str = ser.serialize(root)
print("Serialized Output:", serialized_str)
# Output: "3,9,N,N,20,15,N,N,7,N,N"

ans = deser.deserialize(serialized_str)
print("Deserialized Root Value:", ans.val)
# Output: 3

# T.C: O(N)     --> Working on N nodes
# S.C: O(N)     --> Recursive Call-Stack used for N elements
```

---

## 12. LeetCode 208: Implement Trie (Prefix Tree) (Medium)

* **Identified Pattern Upfront:** Trie
* **Time Taken:** 2 minutes
* **Solution Folder:** [`../../Design/208.%20Implement%20Trie%20(Prefix%20Tree)/`](../../Design/208.%20Implement%20Trie%20(Prefix%20Tree)/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/implement-trie-prefix-tree/submissions/2147450444)

### Code Solution

```python
class Trie:

    def __init__(self):
        # Children array
        self.children = [None] * 26
        # Indicating end of word
        self.is_terminal = False
        

    def insert(self, word: str) -> None:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                curr.children[index] = Trie()

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char, mark insertion as end
        curr.is_terminal = True


    def search(self, word: str) -> bool:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                return False

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char, mark searching as end
        return curr.is_terminal
        

    def startsWith(self, prefix: str) -> bool:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in prefix:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                return False

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char of prefix, mark searching as end
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))   # True
print(obj.search("app"))     # False
print(obj.startsWith("app")) # True
obj.insert("app")
print(obj.search("app"))     # True

"""
None
None
True
False
True
None
True
"""

# T.C: O(26 • L • N) --> Looping through word and working for 26-size for each char
# S.C: insert() → O(26 • L) --> search / startsWith  → O(1)
```

---

## 13. LeetCode 211: Design Add and Search Words Data Structure (Medium)

* **Identified Pattern Upfront:** Trie
* **Time Taken:** 18 minutes
* **Solution Folder:** [`../../Design/211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure/`](../../Design/211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/2147467709)

### Code Solution

```python
class WordDictionary:

    def __init__(self):
        # Children array
        self.children = [None] * 26
        # Indicating end of word
        self.is_terminal = False


    def addWord(self, word: str) -> None:
        # Pointer for traversal
        curr = self

        # Looping through word
        for char in word:
            # Get index
            index = ord(char) - ord("a")

            # If child doesn't exists, create new one
            if not curr.children[index]:
                curr.children[index] = WordDictionary()

            # If exists, move pointer to it's children
            curr = curr.children[index]

        # After last char, mark insertion as end
        curr.is_terminal = True


    def search(self, word: str) -> bool:
        def dfs(i, node):
            # Pointer for traversal
            curr = node

            for j in range(i, len(word)):
                # Current word
                char = word[j]

                # WILDCARD case
                if char == ".":
                    for child in curr.children:
                        # If child, recursively check for rest of branch
                        if child and dfs(j+1, child):
                            return True

                    return False

                # Standard letter
                else:
                    # Get index
                    index = ord(char) - ord("a")
        
                    # If child doesn't exists, create new one
                    if not curr.children[index]:
                        return False
        
                    # If exists, move pointer to it's children
                    curr = curr.children[index]
        
            # After last char, mark searching as end
            return curr.is_terminal

        return dfs(0, self)

    
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))    # False
print(obj.search("bad"))    # True
print(obj.search(".ad"))    # True
print(obj.search("b.."))    # True

'''
None
None
None
False
True
True
True
'''

# obj.addWord("a")
# obj.addWord("a")
# print(obj.search("."))    # True
# print(obj.search("a"))    # True
# print(obj.search("aa"))    # False
# print(obj.search("a"))    # True
# print(obj.search(".a"))    # False
# print(obj.search("a."))    # False

'''
None
None
True
True
False
True
False
False
'''

# T.C: addWord() --> O(L) || search() --> Wildcard:Worst-case O(26^d * L), No Wild-card:O(L)
# S.C: O(N * L)
```

---

## 14. LeetCode 212: Word Search II (Hard)

* **Identified Pattern Upfront:** Trie / Backtracking
* **Time Taken:** 49 minutes
* **Solution Folder:** [`../../Trie/212.%20Word%20Search%20II/`](../../Trie/212.%20Word%20Search%20II/)
* **Submittion Link:** [`Link`](https://leetcode.com/problems/word-search-ii/submissions/2148337746)

### Code Solution

```python
from typing import List

class TrieNode:
    def __init__(self):
        # Children array
        self.children = [None] * 26
        # Indicating end of word
        self.word = None

    def insert(self, words):
        
        for i in range(len(words)):
            curr = self
            word = words[i]
            for j in range(len(word)):
                # Get index
                index = ord(word[j]) - ord("a")

                # If child doesn't exists, create new one
                if not curr.children[index]:
                    curr.children[index] = TrieNode()

                # If exists, move pointer to it's children
                curr = curr.children[index]

            # After last char, mark insertion as end
            curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        # Final answer array
        result = []

        trieNode = TrieNode()
        trieNode.insert(words)

        def dfs(r, c, node):
            # Edge cases: Out of bound + visited
            # if (r < m and r >= m and c < n and c >= n) or board[r][c]:
            if (r < 0 or c < 0 or r >= m or c >= n) or board[r][c] == "#":
                return

            # Get index
            index = ord(board[r][c]) - ord("a")

            # If not present
            if not node.children[index]:
                return

            # Pointer for traversal
            curr = node.children[index]

            # If word found in TrieNode, add it to result
            if curr.word:
                result.append(curr.word)
                # Mark as None
                curr.word = None

            # Storing in temp + marking as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Recursive call on all 4 directions :DOWN, UP, RIGHT, LEFT
            dfs(r+1, c, curr)
            dfs(r-1, c, curr)
            dfs(r, c+1, curr)
            dfs(r, c-1, curr)

            # UNDO: Place original character
            board[r][c] = temp


        # Passing i,j to dfs()
        for i in range(m):
            for j in range(n):
                dfs(i, j, trieNode)

        return result


obj = Solution()
print(obj.findWords(
    [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]], ["oath", "pea", "eat", "rain"]
))      # ["eat", "oath"]
print(obj.findWords(
    [["a","b"], ["c","d"]], ["abcb"]
))      # []

# T.C: O(M ∗ N ∗ 4^L)   --> Nested looping on grid + checking 4 directions for L length word
# T.C: O(S)             --> Trie + result array
```