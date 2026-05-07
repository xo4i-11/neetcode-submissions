# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node, key):
            #base case
            if node is None:
                return None
            
            #SEARCHING PHASE
            if key < node.val:
                #think about: dfs will delete and return the new head. we gonna assign that new head to node.left
                node.left= dfs(node.left, key)
            
            elif key > node.val:
                node.right= dfs(node.right, key)

            else:
                if node.right is None and node.left is None:
                    return None
                
                if node.right and node.left is None:
                    return node.right
                
                if node.left and node.right is None:
                    return node.left
                
                if node.left and node.right:
                    curr = node.right
                    
                    while curr.left:
                        curr= curr.left
                    
                    node.val = curr.val
                    node.right = dfs(node.right, node.val)
                
            return node
        
        return dfs(root, key)
        
            
            

                

            
        
    

                    


                    




"""
idea dfs:
    what are we given and what we need to return:
        + given a node and key, return the root, while also delete the key if possible
        + we delete the key. if the node exist in tree -> delete. else -> do nothing
    
    what is the simpliest case:
        + if the tree is None, no need to delete and return None
    
    if it works normal, there will be 3 case that we need to care about:
        Phase 1: search for the delete node 
            + if key < root.val => move left
            + if key > root.val => move right

            Phase 2: delete the found node
            + if node.val = root.val => found the node now delete (there will be 3 case):
                # if the deleted node have no left child => return right child
                # if the deleted node have no right child => return left child
                # if the delted node have both:
                    first we move to the right child
                    the idea is to find the left most node from the right child, replace deleted node with that, then delete that left most
            
"""