# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #use dfs search for lca
        curr = root

        #base case
        if root is None:
            return None
        
        #for now, the root is not None => we need check if:
        #   + p, q are both on the left => we move left
        #   + p, q are both on the right => move right
        #   + else: p, q are splitted => return the node

        left_subtree= self.lowestCommonAncestor(curr.left,p,q)
        right_subtree= self.lowestCommonAncestor(curr.right,p,q)



        if p.val < curr.val and q.val < curr.val:
            return left_subtree
        elif p.val > curr.val and q.val > curr.val:
            return right_subtree
        else:
            return curr
        


        

            



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














