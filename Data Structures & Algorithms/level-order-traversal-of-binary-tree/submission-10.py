# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        track = deque()
        track.append(root)

        while track:
            size = len(track)
            l = []

            for i in range(size):
                front = track.popleft()

                if front.left:
                    track.append(front.left)
                if front.right:
                    track.append(front.right)

                l.append(front.val)

            result.append(l)

        return result