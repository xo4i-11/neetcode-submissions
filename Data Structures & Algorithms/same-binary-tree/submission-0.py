# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case
        if p is None and q is None:
            return True
        
        if p and not q or q and not p:
            return False
        
        if p.val != q.val:
            return False
        
        
        left_subtree= self.isSameTree(p.left, q.left)
        right_subtree= self.isSameTree(p.right, q.right)

        return left_subtree and right_subtree











"""
idea: 
    we are given 2 head of the tree
    - we can use dfs to discover left and right subtree:
        + recursively compare left node of p to left node of q
        + recursively compare right node of p to right node of q

    - base case: 
    + if both = None: true 
    + if they the same: true
    + if they are not: false



"""
        