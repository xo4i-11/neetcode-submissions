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









"""
problem: 
    - prereq[i] = [a,b] => we must take "b" first, then take "a"
    - numCourses: total of course, label from 0 -> numCourses -1
    - return True if possible to finish all
    - return False otherwise

idea:
    since the curr class depends on preq => they must be in topo order -> kahn algo
    - for kahn algo:
        + we need to find class that have no preq 
        => we use hashmap such that: key = curr course, val = number of preq

        + we need to build adj list, where key = vertex, val = neighbor

        + add all class with preq = 0 to the queue
        + then do a bfs






"""



def course_schedule(numCourses, prerequisites):
    indegree = {}
    graph = defaultdict(list)

    # init all course entries
    for course in range(numCourses):
        indegree[course] = 0
    
    # find the indegree
    # build the graph
    for course, prereq in prerequisites:
        indegree[course] +=1
        graph[prereq].append(course)

    queue = deque()

    # add course with indegree = 0 to queue
    for course in indegree:
        if indegree[course] == 0:
            queue.append(course)
    

    res = []

    while queue:
        node = queue.popleft()
        res.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)
    
    if len(res) == numCourses:
        return True
    return False
        

        

    
            
    




    











































