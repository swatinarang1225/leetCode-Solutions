# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        def InorderPrint(root):
            
            if root.left!=None:
                InorderPrint(root.left)
            output.append(root.val)
            if root.right!= None:
                InorderPrint(root.right)
         
        if root!= None:
            InorderPrint(root)
            return output
        else:
            return []
