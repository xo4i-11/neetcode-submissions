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




# using topo sort (kahn algorithm)


def course_schedule(numCourses, prerequisites):
    # first, we need to create a graph, where the key is the vertex, val is the neighbor
    graph = defaultdict(list)
    
    #indegree to track how many indegree a node have
    indegree = [0] * numCourses
    
    for a,b in prereqisites:
        graph[b].append(a)
        indegree[a]+=1
    
    #after making a graph, we wanna do kahn algo by adding all vertex with indegree=0 to queue
    queue = deque()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    #start removing all node with 0 indegree, mark as finished and track the number
    finish = 0
    while queue:
        node = queue.popleft()
        finish +=1

        for neigh in graph[node]:
            indegree[neigh]-=1
            if indegree[neigh]==0:
                queue.append(neigh)

    if finish == numCourses:
        return True
    else:
        return False



















