# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)

        res=[]

        while queue:
            #track the number of node in that level
            node_count= len(queue)
            level=[]
            for i in range (node_count):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res
                
            

        

            
            




"""
ideas: binary tree level => use bfs:
    when we do bfs:
        - we first track the len of the queue to find num of node in a level
        - loop through n node in that level:
            + add to the level_list
        - after that, add the level_list to res_list
    





"""
        