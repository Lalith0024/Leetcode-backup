# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:   # no left child
                return root.right
            elif not root.right:  # no right child
                return root.left
            else:
                # Node has two children → find inorder successor (smallest in right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                # Delete the inorder successor
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

