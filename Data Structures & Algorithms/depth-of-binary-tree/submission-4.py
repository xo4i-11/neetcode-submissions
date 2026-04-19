# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#return a value
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr= root

        #base case: when the tree is empty
        if curr is None:
            return 0
        
        left_path= self.maxDepth(root.left)
        right_path= self.maxDepth(root.right)

        if left_path>right_path:
            return 1+ left_path
        else:
            return 1+right_path
        
        

