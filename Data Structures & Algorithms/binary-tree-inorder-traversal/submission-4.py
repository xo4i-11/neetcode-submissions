# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def inorder(node):
            #base case:
            if node is None:
                return 
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res


    """
    ideas:
        simple DFS problem. 
        Since it is a in order traversal => follow LnR

    """ 














"""
dfs inorder traversal
"""

def dfs_inorder(root):
    res=[]


    #travsere to the leaf
    def dfs_helper(node):
        #base
        if node is None:
            return 
        
        dfs_helper(node.left)
        res.append(node)
        dfs_helper(node.right)

        return 
    
    dfs_helper(root)
    return res
        

                


































