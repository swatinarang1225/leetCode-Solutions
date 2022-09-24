# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def PathList(self,root,t_sum,lst,result):
    
        if root.left is None and root.right is None:
            if root.val == t_sum:
                result += [lst+[root.val]]
                
        if root.left:
            self.PathList(root.left,t_sum-root.val,lst+[root.val],result)
        if root.right:
            self.PathList(root.right,t_sum-root.val,lst+[root.val],result)
        
        return result
            
    
    
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        Lst =[]
        result = []
        if root is None:
            return []
        return self.PathList(root,targetSum,Lst,result)
