# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # deal with depth=1 first
        if depth == 1:
            return TreeNode(val=val, left=root)  # simply make the root node a left child of the new node
        
        def dfs(node, level):
            if level == depth - 1:  # per problem description, check if current depth (i.e. level) is at depth-1
				# if so, check left and right children
				# if left child exists (we'll call it the old left child), create a new node of value val and make the old left child the left child of the new node.
				# else (i.e. the left child doesn't exist), create a new leaf node of value val and set it as the left child
				# same for right child
                node.left = TreeNode(val, left=node.left) if node.left else TreeNode(val)
                node.right = TreeNode(val, right=node.right) if node.right else TreeNode(val)
                return node
            else:  # current depth is not depth-1 --> check left and right children recursively
                if node.left: node.left = dfs(node.left, level+1)
                if node.right: node.right = dfs(node.right, level+1)
                return node
            
        # add row
        root = dfs(root, 1)  # call dfs starting from the root which is at level/current depth=1
        return root
