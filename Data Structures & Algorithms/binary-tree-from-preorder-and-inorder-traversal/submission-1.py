# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. store value -> index in inorder
        hashmap = {}

        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        # keep track of where we are in preorder
        self.pre_idx = 0

        # left and right ptr in inorder
        def dfs(l,r):
            if l > r:
                return None
            
            #root is the first node of preorder
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx +=1
            
            #track the current root in inorder (root in inorder separate left and right substree)
            mid = hashmap[root.val]

            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(inorder)-1)


            






"""
problem:
    - preorder is an int array store: node -> left -> right
    - inorder is an int array store: left -> node -> right
    - both are same size, unique val

    => rebuild binary tree from those order and return root


idea:
    - since the 2 array are int => we have to build the node from 
    
    - 1) Pre-order will give us the root
    - 2) In-order will give us the left and right subtree
    - example from 1) and 2):

        +) pre-order = [3, 9, 20, 15, 7]
        => we know that 3 is the root

        +) in-order = [9, 3, 15, 20, 7] 
        => we know that [9] is in left-subtree and 
        [15,20,7] right subtree of the root


    
    
"""






















