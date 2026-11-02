# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        track = []
        output = []
        curr = root

        while track or curr:
            while curr:
                track.append(curr)
                curr = curr.left

            curr = track.pop()
            output.append(curr.val)
            curr = curr.right

        return output