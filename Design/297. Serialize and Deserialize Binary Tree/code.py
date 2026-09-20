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