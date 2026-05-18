# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        check=[True]

        #does not return, it is used to update the global var
        #low is the left limit and high is the right limit of
        #since the child not only need to smaller or bigger than its parent, but also need to satisfy the parent of parent
        def dfs(node, left, right):
            #base case
            if node is None:
                return 
            
            #false case
            if node.val <= left or node.val >= right:
                check[0]=False
                return 
            
            #go left => gotta be < node.val => assign to the "right"
            dfs(node.left, left, node.val)

            #go right => gotta be > node.val => assign to the "left"
            dfs(node.right,node.val,right)

            return 
        
        dfs(root, float('-inf'), float('inf'))
        return check[0]
            

            
            

            


        
            
            
            


            


        






"""
idea: to check if its valid bst or not, we need to care abt the node, the left, the right
since BST means we need to make sure that the left subtree < parent, right subtree < parent
=> we can do a dfs, check the left, check the right, if not valid then return false


"""