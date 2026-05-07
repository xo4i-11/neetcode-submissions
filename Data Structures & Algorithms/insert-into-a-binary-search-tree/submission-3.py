# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def dfs(node):
            #base case
            if node is None:
                return TreeNode(val)
            
            #if the node is not None, there will be 2 case, left or right
            # => we need to move to either left or right

            if val < node.val:
                node.left= dfs(node.left)
            else:
                node.right= dfs(node.right)
            
            return node

        return dfs(root)



        
            






"""
idea for recursion: 
    - we gonna use dfs to get to the correct node, then insert the val
    - dfs: 
        we wanna assign the node to the correct position while dfs, afterwards return the root

        + base case: if the node is None, return the Node(val)
        + otherwise, there will be 2 case (left or right):
            if the node is larger than the current val, traverse to the right => node.right= recursion(node.right)
            if the node is smaller than current val, traverse to the left => node.left= recursion(node.left)
    
"""




""""

Iterative Sol: 

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            #edge case
            if root is None:
                root = TreeNode(val, None, None)
                return root
            
            node = TreeNode(val, None, None)
            track= root

            while track:
                if node.val > track.val:
                    if track.right is None:
                        track.right= node
                        return root
                    track = track.right
                elif node.val < track.val:
                    if track.left is None:
                        track.left=node
                        return root
                    track = track.left





"""

            
