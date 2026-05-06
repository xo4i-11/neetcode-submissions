# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #return a boolean 
        def dfs(p, q):
            #base case:
            if p is None and q is None:
                return True
            
            if p and q is None or q and p is None:
                return False
            
            if p.val != q.val:
                return False
        
            # when p.val= q.val, we check if left and right are identical
            left_tree = dfs(p.left, q.left)
            right_tree = dfs(p.right, q.right)

            return left_tree and right_tree
        
        return dfs(p,q)
        


"""
run time: O(n)

space complexity: O(h) -> h stand for the height of the tree (the biggest height of the call stack)
best case: O(logn) -> if the tree balanced
worst: O(n) -> if the tree is a linkedlist
"""
    





"""
idea: 
    we are given 2 head of the tree
    - we can use dfs to discover left and right subtree:
        + recursively compare left node of p to left node of q
        + recursively compare right node of p to right node of q

    - base case: 
    + if both = None: true 
    + if they are not equal: false
    



"""
        