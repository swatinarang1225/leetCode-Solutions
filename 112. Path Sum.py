# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def ispathtrue(self,root,targetSum,lst,result):
        if root.left is None and root.right is None:
            if root.val == targetSum:
                result += [lst + [root.val]]
        if root.left:
            self.ispathtrue(root.left,targetSum-root.val,lst+[root.val],result)
        if root.right:
            self.ispathtrue(root.right,targetSum-root.val,lst+[root.val],result)
        
        return result
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        lst =[]
        result = []
        if root is None:
            return False
        
        c =  self.ispathtrue(root,targetSum,lst,result)
        
        if len(c):
            return True
        else:
            return False
