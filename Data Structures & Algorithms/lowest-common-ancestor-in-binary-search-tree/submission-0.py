# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #root is the common ancestor to every node => start at root
        lca = [root]

        #use to update the global var lca
        def dfs_search(root):
            #base case
            if root is None:
                return 

            #
            lca[0] = root
            if root is p or root is q:
                return 

            if root.val > p.val and root.val > q.val:
                dfs_search(root.left)
            
            elif root.val < p.val and root.val < q.val:
                dfs_search(root.right)
            
            else:
                return 
        
        dfs_search(root)
        return lca[0]

        

            

        

            








"""
ideas: we are given a bst => parent.left < parent
                             parent.right > parent


- since the root is the ancestor to everything (called Most Common Ancestor) 
=> we gonna traverse from root until we find a valid ancestor

"""

"""
better approach: Iterative

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


"""














