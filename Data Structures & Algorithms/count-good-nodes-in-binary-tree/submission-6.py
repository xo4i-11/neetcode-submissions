# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count= [0]

        def dfs(node, max_val):
            #base case:
            if node is None:
                return 0
            
            #if node exist, we check if its a good node or not. If good -> count+=1
            if node.val >= max_val:
                count[0]+=1
            
            #do the same for the left and right child
            if node.left:
                dfs(node.left, max(max_val, node.val))
            
            if node.right:
                dfs(node.right, max(max_val, node.val))


        dfs(root, root.val)
        return count[0]

        

            


        




    
        



"""
good nodes is the number of node such that:
    + in the path from root to good node, the node in that path must <= good node (include root)

idea: dfs
    - what we need from the graph to determine if its a good node or not?
        + we need that node
        + we need the max value so far, since good node >= max_node so far
    
    => create a helper that have node and max so far
        - what are given and what will be return:
            + given node and max_so_far, return the number of good node
        
        - base case:
            + if the tree is empty, return 0
        
        - for now, we want to traverse 
        

"""



















