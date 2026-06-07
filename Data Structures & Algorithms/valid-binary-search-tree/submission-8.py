# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        check = [True]

        #low is the left limit and high is the right limit 
        # since the child not only need to be smaller/larger than its parent
        # but it also need to be smaller/larger than its parent' parent

        def dfs(node, low, high):\

            if node is None:
                return 
            if node.val <= low or node.val >=high:
                check[0] = False
                return
        
            
            dfs(node.left, low, node.val)
            dfs(node.right, node.val, high)

            return 

        dfs(root, float('-inf'),  float('inf'))

        return check[0]            


       
            
      
            
            

            







"""
idea:
    + to check if its a valid bst or not, the left subtree gotta be smaller than the parent
    + the right subtree is gotta be larger than the parent

"""
        