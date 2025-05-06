# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def rec(root,lst):
            if root==None:
                return None
            lst.append(root.val)
            rec(root.left,lst)
            rec(root.right,lst)
        rec(root,lst)
        return lst
        
