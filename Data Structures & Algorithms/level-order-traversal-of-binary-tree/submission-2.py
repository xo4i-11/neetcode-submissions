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
        - in order to track the node in the same level: 
            + we remove node in same level 1 by 1, then add their children to the queue
            => track the length of the queue, then remove the exact number of node 
            from queue to ensure the node in the same level
            Basically, the number of node we remove from queue in 1 loop = num of node in that level





"""



def binary_tree_level_order(root):
    if root is None:
        return []

    queue= deque()
    queue.append(root)
    res=[]

    while queue:
        level=[]
        for i in range(len(queue)):
            node = queue.popleft()

            level.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        res.append(level)

    return res





































        