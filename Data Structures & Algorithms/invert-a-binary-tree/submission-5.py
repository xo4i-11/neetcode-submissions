# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #take a node, return root
        def dfs(node):
            #base 
            if node is None:
                return None
            
            #if it works perfect
            node.left, node.right= dfs(node.right), dfs(node.left)

            return node
        
        return dfs(root)
        
        
        

            


    









"""
idea for dfs:
    - what the function take and what it return: 
        + it take a node, return the root
        + when we are at a node, we swap left and right of them 
    - what is the base case:
        + when the node is None -> return None
    - recursive step: assume it works perfectly:
        + node.left= recursive(node.right)
        + node.right= recursive(node.left)
    - Finally, from the contract, we return what:
        + return the root


"""


"""
ideas:  use bfs

    - base case: if root None -> return None
    - bfs data structure: queue
    - do the bfs
"""
def invert_tree(root):
    #base case
    if root is None:
        return None

    queue= deque()
    queue.append(root)

    while queue:
        removed_node= queue.popleft()

        temp= removed_node.left
        removed_node.left= removed_node.right
        removed_node.right=temp

        if removed_node.left:
            queue.append(node.left)
        if removed_node.right:
            queue.append(node.right)

    return root





    



        


































