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

        # 1. DO DFS TO CREATE COPY OF EVERY NODE
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





def clone_graph(node):

    if node is None:
        return None

    #dfs first to assign copy to 
    hashmap={}
    stack=[]
    stack.append(node)
    visited=set()

    while stack:
        removed_node= stack.pop()

        copy_node= Node(removed_node.val)
        hashmap[removed_node] = copy_node

        for neighbor in removed_node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    

    for each_node in hashmap:
        for neighbor in each_node.neighbors:
            new_neighbor = hashmap[neighbor]
            new_node = hashmap[each_node]
            new_node.neighbors.append(new_neighbors)
    
    return hashmap[node]
            






def clone_graph(node):
    if not node:
        return None 
    
    # hashmap: key = old node, val = new copy of that node
    oldToNew = {}

    # dfs is used to copy the graph
    def dfs(node):
        # If we already copied this node, return the copy
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)

        # save it before visiting neighbor
        oldToNew[node] = copy

        # copy all neighbor
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        
        return copy
    
    return dfs(node)
    












def clone_graph(node):
    if node is None:
        return []

    hashmap = {}

    #dfs is used to create the pair in hashmap
    def dfs(node):
        if node in hashmap:
            return hashmap[node]
        
        clone = Node(node.val)
        hashmap[node] = clone

        # 
        for nei in node.neighbors:
            clone.neighbors.append(dfs(nei))
        
        return clone
    
    return dfs(node)



































    
