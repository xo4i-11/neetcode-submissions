class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
        #Create adj list graph
        graph=defaultdict(list)
        #key = vertex, value = list of (neighbor, weight) 
        for u, v, w in times:
            graph[u].append((v,w))
        
        visited = set()
        #create a pqueue/min heap
        minHeap=[]
        minHeap.append((0, k))
        min_time = 0

        #Dikjstra algo
        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)
            min_time = weight

            for neighbor, neighbor_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight + neighbor_weight, neighbor))
        
        if len(visited) == n:
            return min_time
        else:
            return -1

        
    

            



"""
idea:
    - we are trying to find the shortest path from the starting node to the last node
    - the edge also have weight
    => we need to use dikstra algorithm

dikstra algorithm is basically using a priority queue (aka a min heap) since it priority the 
shortest edge

"""