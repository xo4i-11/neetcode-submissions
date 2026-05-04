# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check= None
        
        
        #helper
        def dfs_find_height(node):
            #base case
            if node is None:
                return 0
            
            left= dfs_find_height(node.left)
            right= dfs_find_height(node.right)

            diff = abs(right-left)

            if diff> 1:
                self.check= False
                
            
            return 1+ max(left, right)
        
        dfs_find_height(root)
        
        if self.check == False:
            return False
        else:
            return True

        







"""
idea: - height-balanced tree means diff between left and right subtree's height of every node <=1
    idea: 
      
    - use dfs: find left and right subtree height
    - if diff >=1 => return False
    - else: return false

"""