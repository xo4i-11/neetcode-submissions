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
            #base case
            if node is None:
                return 0
            
            # now we get to the non empty node
            #first, check if its a good node
            good_node = 0
            if node.val >= max_val:
                good_node = 1
            
            #update the max value so far
            max_val = max(max_val, node.val)
            good_node+= dfs(node.left, max_val)
            good_node+= dfs(node.right, max_val)

            return good_node
        
        return dfs(root, root.val)




    
        







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
        
        the number of good nodes = 1 (root) + left_good_nodes + right_good_nodes
        - consider everything is correct, use the recursion:
            if node.right > max_count:
            left_count = recursion(node.left)
            right_count= recursion(node.right)
        


"""



















