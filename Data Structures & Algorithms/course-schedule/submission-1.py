class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        #build graph
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        

        # add all indegree = 0 to the queue
        queue = deque()

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        # kahn algo
        finish = 0
        while queue:
            node = queue.popleft()
            finish+=1

            for neighbor in graph[node]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        
        if finish == numCourses:
            return True
        else:
            return False








"""
since in [0,1], 0 depends on 1, 0  => we can do topo sort (kahn algo)

idea:
    - build a graph, with key be the elem, val be the list that store prerequisites





"""