# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxi = float("-inf")
        level = 0
        max_level = 0

        q = [root]

        while q:
            leng = len(q)
            sums = 0
            level += 1              # current level

            for i in range(leng):
                popped = q.pop(0)
                sums += popped.val
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

            if sums > maxi:         # track level of max sum
                maxi = sums
                max_level = level

        return max_level

