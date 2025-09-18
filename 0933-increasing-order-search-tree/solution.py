# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def rec(node):
            if node is None:
                return None
            rec(node.left)
            arr.append(node.val)
            rec(node.right)
        rec(root)
       
        root = TreeNode(arr[0])
        curr = root
        for i in arr[1:]:
            temp = TreeNode(i)
            curr.right = temp
            curr.left = None
            curr = curr.right
        return root

