# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_lis = q_lis=[]
        lis = []
        def traverse(root):
            if root:
                lis.append(root.val)
                traverse (root.left)
                traverse (root.right)
            else:
                lis.append("null")
            
            return lis
                
        p_lis = traverse(p)
        lis=[]
        q_lis = traverse(q)
        if p_lis == q_lis:
            return True
        else:
            return False
       
        
        
