# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def rec(root):
            if root is None:
                return None
            rec(root.left)
            arr.append(root.val)
            rec(root.right)

        rec(root)

        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] + arr[r] == k:
                return True
            elif arr[l] + arr[r] > k:
                r -= 1
            else:
                l += 1

        return False

