# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            nonlocal balanced
            if not -1 <= left - right <= 1:
                balanced = False

            return 1 + max(left, right)

        height(root)

        return balanced