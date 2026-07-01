class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
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




