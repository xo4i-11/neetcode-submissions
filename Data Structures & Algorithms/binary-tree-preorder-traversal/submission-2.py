# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def preorder(node):
            #base case
            if node is None:
                return
            
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res









"""
ideas:

it is a DFS pre order traversal => nLR


"""

def dfs_preorder(root):
    visited=[]

    def helper(node):
        if Node is None:
            return
        
        visited.append(node.val)
        helper(node.left)
        helper(node.right)

        return
    
    helper(root)
    return visited

        

































