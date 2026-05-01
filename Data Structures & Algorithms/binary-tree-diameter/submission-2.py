# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        # helper to find height => return the height of subtree
        def dfs_find_height(node):
            #base case
            if node is None:
                return 0
            
            #left and right subtree height
            left = dfs_find_height(node.left)
            right = dfs_find_height(node.right)

            # update global diameter
            self.longest_path = max(self.longest_path, left + right)

            # return height
            return 1 + max(left, right)

        dfs_find_height(root)
        return self.longest_path

    
    


"""
ideas:
    they are asking for the longest path between 2 nodes

    Imagine you are at a node => the longest path will be: left_subtree_height + right_subtree_height
    => find height of each subtree => use a helper method to find height of the tree


"""


        






































        
        
        