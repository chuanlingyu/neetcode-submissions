# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            return left + 1 if left > right else right + 1

        return height(root)