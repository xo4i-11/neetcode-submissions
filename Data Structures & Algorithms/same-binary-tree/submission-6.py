# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check = [True]

        def dfs(node1, node2):
            if not node1 and not node2:
                return 

            if node1 and not node2:
                check[0] = False
                return 

            if node2 and not node1:
                check[0] = False
                return

            if node1.val != node2.val:
                check[0] = False
                return
            
            dfs(node1.left,node2.left)
            dfs(node1.right, node2.right)
            return 
        
        dfs(p,q)
        return check[0]
        
            
            




"""
Same binary tree if:   
    + root equals,
    + left and right equal




"""



def same_bt(p,q):
    check = True

    def dfs(node1, node2):
        nonlocal check

        if node1 is None and node2 is None:
            return 

        if node1 is None and node2:
            check = False
            return
        
        if node1 and node2 is None:
            check = False
            return 
        
        if node1.val != node2.val:
            check = False
            return 
        
        dfs(node1.left, node2.left)
        dfs(node1.right, node2.right)

        return 
    
    dfs(p,q)
    return check






























        
        
















        
        