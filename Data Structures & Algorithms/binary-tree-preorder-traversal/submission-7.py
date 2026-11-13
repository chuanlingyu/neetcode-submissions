# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output

        track = []
        track.append(root)

        while track:
            top = track[-1]
            output.append(top.val)
            track.pop()
            if top.right:
                track.append(top.right)

            if top.left:
                track.append(top.left)


        return output