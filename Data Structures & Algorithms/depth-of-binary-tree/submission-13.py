# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            #base case
            if node is None:
                return 0
            
            #recursive step, we want it to return the node count
            count_left= helper(node.left)
            count_right= helper(node.right)

            #return the bigger depth
            return 1 + max(count_left, count_right)
        

        return helper(root)






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

        #return the bigger depth
        return 1 + max(count_left, count_right)
    

    return helper(root)

        








































