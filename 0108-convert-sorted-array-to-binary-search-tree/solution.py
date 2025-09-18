# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # helper function to build BST recursively
        def buildBST(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # recursively build left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            
            return root
        
        return buildBST(0, len(nums) - 1)

