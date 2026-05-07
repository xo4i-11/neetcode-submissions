# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if node is None:          # 2. base case
                return None

            if p.val < node.val and q.val < node.val:
                return dfs(node.left)   # 3. recursive + 4. return

            if p.val > node.val and q.val > node.val:
                return dfs(node.right)  # 3. recursive + 4. return

            return node               # 4. return — split point found
          
        return dfs(root)


        






"""
CLAUDE APPROACH:
    we will use dfs
    - what will the function takes, do and what it return: 
        + the function take a node, and return the LCA
    - what is the easiest case that we can return the lca:
        + if the tree is empty, the lca must be empty
    - if it works perfect:
        + if p and q in left -> LCA lives in left subtre
        + if p and q in right -> LCA lives in right subtree
        + else if p and q splitted -> return LCA





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














