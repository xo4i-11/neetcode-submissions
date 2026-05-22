"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        start= node
        old_to_new= {}
        
        stack= [start]
        visited= set()
        visited.add(start)

        #this step is to create copy of every node
        while stack:
            node = stack.pop()

            #create copy
            copy_node = Node(node.val)
            old_to_new[node] = copy_node

            #loop through every neigbor of og node
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
            
        
        #now, we assign the pointer to those copy node
        for old_node, new_node in old_to_new.items():
            for neighbor in old_node.neighbors:
                new_neighbor = old_to_new[neighbor]
                new_node.neighbors.append(new_neighbor)

        
        return old_to_new[start]


    
        



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

    
    - we use hashmap, where key= node and value= copy_node
    - we recursivelt go to next node:
        + if the node is not in the hashmap => create a copy and store in hashmap
"""