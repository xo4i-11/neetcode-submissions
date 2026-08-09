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








"""
lowest common ancestor

idea:
the common ancestor of 2 node is always the root
we will do dfs from the root, have the left and right limit init = inf 
we traverse to left and right to find 

"""
def lowest_common(root, p, q):
    lowest = root

    def dfs(node):
        nonlocal lowest

        if node is None:
            return
        
        if node.val > p.val and node.val > q.val:
            dfs(node.left)
            return 
        
        if node.val < p.val and node.val < q.val:
            dfs(node.right)
            return 
        
        lowest = node
    
    dfs(root)
    return lowest
        

















