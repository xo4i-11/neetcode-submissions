# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            #edge case
            if root is None:
                root = TreeNode(val, None, None)
                return root
            
            node = TreeNode(val, None, None)
            track= root

            while track:
                if node.val > track.val:
                    if track.right is None:
                        track.right= node
                        return root
                    track = track.right
                elif node.val < track.val:
                    if track.left is None:
                        track.left=node
                        return root
                    track = track.left
                            

            
