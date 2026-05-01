# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # update global diameter
            self.result = max(self.result, left + right)

            # return height
            return 1 + max(left, right)

        dfs(root)
        return self.result

    
    





"""
ideas:
    use dfs, discover left subtree and right subtree
    the answer gonna be node count of left + right subtree
"""








































        
        
        