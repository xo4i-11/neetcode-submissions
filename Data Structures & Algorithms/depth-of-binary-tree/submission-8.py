# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        if curr is None:
            return 0
        
        left_depth= self.maxDepth(curr.left)
        right_depth=self.maxDepth(curr.right)

        if left_depth > right_depth:
            return 1 + left_depth
        else:
            return 1+ right_depth













"""
idea: find the depth
    - create a value to track the depth
    - first node have the depth = 1
    - depth is the number of node along the path

    => use dfs. first, discover left subtree, then right subtree
    after all, take the longer one
"""

def max_depth(root):


    def helper(node):
        #base case
        if node is None:
            return 0
        
        #recursive step, we want it to return the node count
        count_left= helper(node.left)
        count_right= helper(node.right)

        if count_left >= count_right:
            return 1+ count_left #count left= number of node in left subtree; 1 mean the parent node
        else:
            return 1+ count_right
    

    return helper(root)

        








































