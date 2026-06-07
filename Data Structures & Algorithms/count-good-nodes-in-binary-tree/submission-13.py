# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        #not return
        def dfs(node, lim):
            if node is None:
                return 

            if node.val >= lim:
                count[0]+=1

            new_lim = max(lim, node.val)
            dfs(node.left, new_lim) 
            dfs(node.right, new_lim)

            return 
        
        dfs(root, root.val)
        return count[0]
        






"""
idea:
    - good node if the path from root -> that node has NO node > that node
    
    => to do:
        + create a value count as global var
        


"""
        