class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if there is 0 or 1 nodes
        if n == 0 or n == 1:
            return n
        
        # if there is no edges
        if len(edges) == 0:
            return n
        
        graph = defaultdict(list)

        for node, nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)

        visited = set()


        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

            return 
            

        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count +=1
        
        return count
        







def create_graph(n,edges):
    graph={}

    for i in range(n):
        graph[i]=[]
    
    for start,end in edges:
        graph[start].append(end)
        graph[end].append(start)
    
    return graph















"""
idea:
    -  build a graph, traverse from every node. count how many time we need to do bfs => that is
    the number of connected component
"""


def connected_comp(n, edges):
    # if there is 0 or 1 nodes
    if n == 0 or n == 1:
        return n
    
    # if there is no edges
    if len(edges) == 0:
        return n
    
    graph = defaultdict(list)

    for node, nei in edges:
        graph[node].append(nei)
        graph[nei].append(node)

    visited = set()


    def dfs(node):
        if node in visited:
            return 
        
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)

        return 


    count = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            count +=1
    
    return count














    