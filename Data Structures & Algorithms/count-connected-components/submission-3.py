class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #when there is 0 or 1 node
        if n == 0 or n==1:
            return n
        
        #when there is >=1 node but no edges
        if len(edges)==0:
            return n

        #create a graph
        graph=create_graph(n,edges)

        visited=set()
        
        #connected component count
        count=0

        def bfs(node):
            queue=deque()
            queue.append(node)

            while queue:
                rm_node= queue.popleft()

                if rm_node not in visited:
                    visited.add(rm_node)
                
                for neighbor in graph[rm_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)



        #loop through every node that is not visted to do bfs
        for node in graph:
            if node not in visited:
                bfs(node)
                count+=1
        
        return count
        







def create_graph(n,edges):
    graph={}

    for i in range(n):
        graph[i]=[]
    
    for start,end in edges:
        graph[start].append(end)
        graph[end].append(start)
    
    return graph

    