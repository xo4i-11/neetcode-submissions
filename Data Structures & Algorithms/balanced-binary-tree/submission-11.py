# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = [True]

        #find the height
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) > 1:
                check[0] = False
            
            return 1 + max(left, right)
        
        dfs(root)
        return check[0]
            
        
            





"""
idea:
    - the tree is balanced if: 
        - left and right subtree of every node differ in height by no more than 1

    => to do:
        - dfs, for each node, if the abs(right-left) > 0 => false
"""







def is_balance(root):

    check = True

    def dfs(node):
        nonlocal check 

        if check == False:
            return 0

        if node is None:
            return 0
        
        left= dfs(node.left)
        right = dfs(node.right)

        if abs(left-right) > 1:
            check = False
            

        return 1 + max(left, right)
    
    dfs(root)
    return check 










#balanced if for every node, the diff in height if left and right subtree <=1
#for every node, we will check if they are balance or not
def balance_bst(root):
    is_balanced = True

    def dfs(node):
        nonlocal is_balanced
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        if abs(right-left) > 1:
            is_balanced = False
        
        return 1 + max(left, right)
    
    dfs(root)
    return is_balanced
        
        
        































