class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph amd indegree
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        #doing kahn algo -> add all vertex with indegree =0
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        finish = 0
        output = []

        while queue:
            node = queue.popleft()
            output.append(node)
            finish +=1

            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)

        
        if finish != numCourses:
            return []
        else:
            return output





"""
problem:
    - 

"""



def course_schedule(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = {}

    # init the indegree for every node
    for course in range(numCourses):
        indegree[course] = 0

    # build graph
    # find indegree
    for course, prereq in prerequisites:
        indegree[course] += 1
        graph[prereq].append(course)   

    # add "indegree = 0" course to the queue
    queue = deque()
    for course in indegree:
        if indegree[course] == 0:
            queue.append(course)
    

    res = []
    finish = 0

    while queue:
        node = queue.popleft()
        res.append(node)
        finish +=1

        for nei in graph[node]:
            indegree[nei] -=1

            if indegree[nei] == 0:
                queue.append(nei)
    
    if finish != numCourse:
        return []
    return res





























