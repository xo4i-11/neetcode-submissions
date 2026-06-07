# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # store in order traversal list of node
        arr = []

        # in order traversal
        def dfs(node):
            if node is None:
                return 
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

            return 
        
        dfs(root)
        
        #return the elem at kth idx
        return arr[k-1]
        
        
        




"""
idea:
    we use dfs
    do in order traversal since it ensure that we explore most left, then the right 




"""
        