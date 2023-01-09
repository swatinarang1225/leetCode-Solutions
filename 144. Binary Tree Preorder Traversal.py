# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def print(self,root,li):
        if root is not None:
            li.append(root.val)
            self.print(root.left,li)
            self.print(root.right,li)
        else:
            return None
        


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.print(root,output)
        print(output)
        return output
        
