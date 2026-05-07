# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue= deque()
        queue.append(root)

        res=[]
        while queue:
            level=[]
            
            for i in range(len(queue)):
                node= queue.popleft()   
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level[-1])
        
        return res











"""
idea:
    use bfs: 
    discover level by level
    if at a level, there is right child => append to the global lst and skip checking left
    if at a level there is only left child => append to the global lst




"""
        