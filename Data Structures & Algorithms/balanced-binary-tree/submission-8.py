# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #represent global variable 
        balanced=[True]

        #dfs to find height 
        def dfs_find_height(node):

            #base case
            if node is None:
                return 0
            
            #left and right height
            left_height=  dfs_find_height(node.left)
            right_height=  dfs_find_height(node.right)

            diff= abs(left_height-right_height)

            #if not balanced
            if diff >1:
                balanced[0]=False
                #return a dummy value
                return 0
            
            return 1+ max(left_height,right_height)

        
        dfs_find_height(root)
        return balanced[0]






"""
idea: - height-balanced tree means diff between left and right subtree's height of every node <=1
    idea: use dfs
    - we have to check every single node  to see if it is balanced or not
    - balanced =[True] is the global variable
    - find the height of the left and right subtree, then compare
    - if its not balance => set the global var "balenced" to False, then return dummy value to terminate 


    

"""