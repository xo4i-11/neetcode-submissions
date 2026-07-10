class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create a graph (adj list)
        # key = vertex
        # value = (neighbor, division(aka weight))
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        

        #ex : a/b => src = a, target = b and we must find a way from a->b:
        #   + for example: a-> c -> b
        def bfs(src, target):
            
            #handle invalid var 
            if src not in graph or target not in graph:
                return -1

            queue = deque()
            visited = set()

            # (src,1): 1 is the current product
            queue.append((src, 1))
            visited.add(src)

            while queue:
                node, weight = queue.popleft()
                
                if node == target:
                    return weight

                for nei, nei_weight in graph[node]:
                    if nei not in visited:
                        queue.append((nei,weight * nei_weight))
                    

            return -1 



        res = []

        for q in queries:
            division = bfs(q[0], q[1])
            res.append(division)
        
        return res






"""
idea:
    - equations[i] = [Ai, Bi]
    - values[i] = Ai/Bi
    - queries[j] = [Cj, Dj]
    => find the answer to all queries. If could not determine => return -1.0

idea:
    - map all numerator to valid denominator 
    - the edge (must be directed) will store the weight (the division):
        + ex: 
                2       3
            a -----> b -----> c
              <-----   <----- 
                1/2      1/3



"""                     