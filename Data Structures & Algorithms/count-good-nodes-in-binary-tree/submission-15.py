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




"""
idea: a node X is good if:
    + the path from root of tree to X contains 0 node > X

approach:
    - Compare node.val with maxSoFar.
    - If node.val >= maxSoFar, it's a good node → count +1.
    - Update maxSoFar:

        maxSoFar = max(maxSoFar, node.val)
        
    - Pass that value to the left and right children. 
"""


def count_good_node(root):
    count = 0

    def dfs(node, limit):
        nonlocal count 

        if node is None:
            return 
        
        if node.val >= limit:
            count +=1
        
        new_limit = max(node, limit)
        dfs(node.left, new_limit)
        dfs(node.right, new_limit)

        return
    
    dfs(root, root.val)
    return count 
            












        
        







































        