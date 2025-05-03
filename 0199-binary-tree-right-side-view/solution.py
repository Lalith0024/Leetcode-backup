# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = []
        q = []
        q.append(root)
        while q:
            temp = []
            for i in range(len(q)):
                popped = q.pop(0)
                temp.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            l.append(temp[-1])
        return l
        
