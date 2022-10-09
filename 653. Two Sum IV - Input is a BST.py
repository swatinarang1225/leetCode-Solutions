# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        order = [root]
        seen = set()

        while order:
            node = order.pop()

            if k - node.val in seen:
                return True

            seen.add(node.val)
            if node.right: order.append(node.right)
            if node.left: order.append(node.left)

        return False
