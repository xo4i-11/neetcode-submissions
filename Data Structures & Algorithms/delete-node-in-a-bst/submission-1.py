# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None

        if key> root.val:
            root.right= self.deleteNode(root.right,key)
        elif key < root.val:
            root.left= self.deleteNode(root.left,key)
        else:
            if root.right ==None and root.left==None:
                return None
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left

            
            #find the min of right sub tree
            curr=root.right
            while curr.left:
                curr=curr.left
            
            root.val= curr.val
            root.right = self.deleteNode(root.right,root.val)
        
        return root


            

        