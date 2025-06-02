# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        c=0
        def rec(root):
            nonlocal c
            if root==None:
                return None
            rec(root.left)
            rec(root.right)
            c+=1
        rec(root)
        return c
            
