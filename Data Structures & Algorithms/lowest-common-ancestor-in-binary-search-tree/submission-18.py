# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest = [root]

        def dfs(node):
            if node is None:
                return 
            
            if p.val < node.val and q.val < node.val:
                dfs(node.left)
                return 
            
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
                return 
            
            lowest[0] = node

    
        dfs(root)
        return lowest[0]





"""
idea:
    - find lowest common ancestor:
        + if p and q both < the current ancestor => move left
        + if p and q both > the current ancestor => move right
        + if p < current ancestor < q => choose



"""