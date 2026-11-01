# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        track = []
        cur = root

        while cur or track:
            while cur:
                track.append(cur)
                cur = cur.left
            cur = track.pop()
            output.append(cur.val)
            cur = cur.right

        return output