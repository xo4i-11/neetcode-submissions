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