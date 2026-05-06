# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    #dfs for search
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case
        if subRoot is None:
            return True
        
        if root is None and subRoot:
            return False

        #when the tree and the given subtree are not empty (since its the remaining case after the above conditions)
        #first, check if the subtree in tree and the given subtree are the same:
        if self.is_same_tree(root, subRoot):
            return True
        
        #otherwise, move to the next left or right node of root and comparing 
        left_subtree= self.isSubtree(root.left, subRoot)
        right_subtree= self.isSubtree(root.right, subRoot)

        return (left_subtree or right_subtree)


    #dfs for compare 
    def is_same_tree(self, root, subroot):
        #base case
        if root is None and subroot is None:
            return True
        
        if root and subroot is None or root is None and subroot:
            return False
        
        if root.val != subroot.val:
            return False
        
        #when root.val=subroot.val (since its the only case), we compare its left and right 
        left_tree= self.is_same_tree(root.left, subroot.left)
        right_tree= self.is_same_tree(root.right, subroot.right)

        return left_tree and right_tree






"""
ideas: we use double dfs
    - the main dfs (dfs in isSubtree) is used to search for the correct root
        + base case:
            when there is 0 node in subroot => always true
            when there is 0 node in root but subroot have at least 1 => always false
        
        + recursive step: (it follow the preorder traversal => nLR)
            we recursively check if initial tree and subtree is identcical. if yes => return True (n)
            else:
                we recursively check left (L)
                we recursively check right (R)

                if 1 of them match the subtree, return true

    -  the other dfs (dfs in is_same_tree) is used to validate if subtree of main tree is identical to the given subtree or not:
        + we can do the same to the "Same Tree" leetcode question
        




"""
        