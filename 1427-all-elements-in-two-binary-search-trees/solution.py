# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # make it optimal 
        arr1 = []
        arr2 = []
        def rec(root,arr):
            if root is None:
                return None
            rec(root.left,arr)
            arr.append(root.val)
            rec(root.right,arr)
        rec(root1,arr1)
        rec(root2,arr2)
        return sorted(arr1+arr2)
        
