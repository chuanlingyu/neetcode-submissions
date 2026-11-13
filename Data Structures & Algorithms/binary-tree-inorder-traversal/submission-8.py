# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output

        track = []
        curr = root

    
        while curr:
            track.append(curr)
            curr = curr.left

        while track:
            top = track[-1]
            output.append(top.val)

            track.pop()
            top = top.right

            while top:
                track.append(top)
                top = top.left

        return output