class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # in a tree, edge = vertex-1
        if len(edges) > n-1:
            return False
        
        # build a graph (undirected graph)
        graph  = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        #used to make sure not traverse back
        visited = set()

        #used to traverse and check if there is a cycle or not
        def dfs(node, parent): #parent is the prev node
            #base case: 
            if node in visited:
                return False
            
            visited.add(node)

            #exploring the neighbor
            for neigh in graph[node]:
                #since it is a undirected graph => if the neighbor of a node is the prev node -> valid -> skip
                if neigh == parent:
                    continue
                
                if dfs(neigh,node) == False:
                    return False
            
            return True
        
        #len(visited) == n used to prevent from a disconnected graph.
        # ex: 1-3-4  2-5
        if dfs(0,-1) and len(visited) == n:
            return True
        return False

                