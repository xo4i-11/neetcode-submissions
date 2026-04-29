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

            


    












"""
ideas:  use bfs

    - base case: if root None -> return None
    - bfs data structure: queue
    - do the bfs
"""
def invert_tree(root):
    #base case
    if root is None:
        return None

    queue= deque()
    queue.append(root)

    while queue:
        removed_node= queue.popleft()

        temp= removed_node.left
        removed_node.left= removed_node.right
        removed_node.right=temp

        if removed_node.left:
            queue.append(node.left)
        if removed_node.right:
            queue.append(node.right)

    return root





    



        


































