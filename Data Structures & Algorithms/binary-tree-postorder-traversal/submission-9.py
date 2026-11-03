# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        track = []
        curr = root
        
        while track or curr:
            if curr: 
                output.append(curr.val)
                track.append(curr)
                curr = curr.right

            else:
                curr = track.pop()
                curr = curr.left

        output.reverse()

        return output