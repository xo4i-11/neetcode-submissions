"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new={}

        def dfs(node):
            #base case
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node]= copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
             
            return copy
        
        if node:
            return dfs(node)
        else:
            return None
        
        



"""
problem: 
    graph displayed as adj list
    nodes are number from 1->n, where n is the total number of nodes in graph
    input node will always be the 1

idea: using dfs
    - use hashmap, key= old node, value =clone node
    - we recursively go to next node:
        + when we first see a node, we create a copy of it
        + we trynna look up the table if the prev node is in the table or not:
            * if its already in => prev node must be neighbor to current node
"""