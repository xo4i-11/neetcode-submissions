# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_subtree = [False]

        #return the if its subtree or not
        def check_subtree(node, subNode):
            if node is None and subNode is None:
                return True 
            
            if node and subNode is None or not node and subNode:
                return False
            
            if node.val != subNode.val:
                return False
            
            left = check_subtree(node.left, subNode.left)
            right = check_subtree(node.right, subNode.right)

            return left and right
        
        def dfs(node):
            if node is None:
                return 
            
            if node.val == subRoot.val:
                if check_subtree(node, subRoot):
                    is_subtree[0] = True
                    return 
            
            dfs(node.left)
            dfs(node.right)
    
        dfs(root)
        return is_subtree[0]

            

        
        


            



"""
idea:
    first, do dfs to find the node, if found the node, do dfs to check if they are the same or not


"""