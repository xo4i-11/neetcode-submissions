class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        #track parents of node 1 -> n
        # initially, their parents are themselves
        parent = [] 
        for i in range(n+1):
            parent.append(i)
        
        #find the root of a node
        def find(node):
            while parent[node] != node: 
                node = parent[node]
            
            return node

        #connect 2 nodes
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                parent[root2] = root1

        for edge in edges:

            node1 = edge[0]
            node2 = edge[1]

            if find(node1) == find(node2):
                return edge

            union(node1, node2)  





"""
idea:

union find:
for example:  1-2-3  4  5 
        => find(1)= find(2) = find(3) = 1

        
idea:
    -   we use union find to detect the cycle
    - for union find: we need to track the root of every node
        + in example 1:
            1 
          / | \
         2  3  4 (3-4 but root of 3 is 1)
        
        2-4 => 1-1 => cycle => that is the thing we wanna return 

"""








"""
union find:
    union(x,y): union the group containing x, y
    find(x): find the group that have x

idea:
    - use union find to keep track of which nodes are already connected.

    - If an edge connects two nodes that already have the same root, 
    => that edge creates a cycle → it's the redundant edge.

"""




def redundant_connection(edges):
    #since there is always a cycle => number of edge = number of nodes
    n = len(edges)

    # 1. assign parent to each node
    # parents: a list that store the parent of node 1-> n
    parents = [0] * (n+1)
    # initially, the node will be its own parent
    for i in range(1, n+1):
        parents[i] = i


    #find parent
    def find(node):
        while parents[node] != node:
            node = parents[node]
        
        return node
    
    # connect 2 group
    def union(node1, node2):
        root1= find(node1)
        root2 = find(node2)

        if root1 != root2:
            parents[root2] = root1
        
    
    for edge in edges:

        node1 = edge[0]
        node2 = edge[1]

        if find(node1) == find(node2):
            return edge

        union(node1, node2) 







'''
For each edge [a,b]:

    find(a)
       ↓
    root1

    find(b)
       ↓
    root2

    same root?
       ↓
   YES → cycle → return [a,b]

   NO → union them



'''














