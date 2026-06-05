# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = [True]

        #find the height
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) > 1:
                check[0] = False
            
            return 1 + max(left, right)
        
        dfs(root)
        return check[0]
            
        
            





"""
idea:
    - the tree is balanced if: 
        - left and right subtree of every node differ in height by no more than 1

    => to do:
        - dfs, for each node, if the abs(right-left) > 0 => false
"""



