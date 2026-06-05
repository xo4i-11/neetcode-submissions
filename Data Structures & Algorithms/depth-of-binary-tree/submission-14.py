# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # the point is to find the height of each node each time we traverse
        def dfs(node):
            #base case
            if node is None:
                return 0
            
            # if its not None
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_height = max(left_height, right_height)

            return 1 + max_height
        
        return dfs(root)







"""
idea: 
    - to determine if the tree max depth is belongs to left or right
    - we need to find the height of left subtree
    - we need to find the height of the right subtree
    - take the max of them



"""
        