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

        queue =deque()
        queue.append(root)

        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level[-1])
        
        return res
        












def right_side_view(root):
    if root is None:
        return []
    
    queue = deque()
    queue.append(root)

    res = []

    while queue:
        level_size = len(queue)
        for i in range(level_size):

            node = queue.popleft()

            if i == level_size -1:
                res.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return res


    



















