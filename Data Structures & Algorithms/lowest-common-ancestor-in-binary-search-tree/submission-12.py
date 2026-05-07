# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)

            if p.val > node.val and q.val > node.val:
                return dfs(node.right)

            return node  # only base case needed

        return dfs(root)


        






"""
CLAUDE APPROACH:
    we will use dfs
    - what will the function takes, do and what it return: 
        + the function take a node, and return the LCA
    - what is the easiest case that we can return the lca:
        + when 





"""


"""
If both left → solve smaller problem on left subtree
If both right → solve on right subtree
If split → return current node
"""


            








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














