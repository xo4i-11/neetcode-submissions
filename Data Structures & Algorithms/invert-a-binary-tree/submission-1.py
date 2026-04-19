# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: #base case
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()

            #swap 2 node in the same level
            temp=node.left
            node.left= node.right
            node.right=temp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

            


    