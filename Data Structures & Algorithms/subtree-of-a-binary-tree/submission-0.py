# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def helper(big_root: Optional[TreeNode], small_root: Optional[TreeNode]) -> bool:
            if not big_root and not small_root:
                return True

            if not big_root or not small_root or big_root.val != small_root.val:
                return False

            return helper(big_root.left, small_root.left) and helper(big_root.right, small_root.right)

        if helper(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)