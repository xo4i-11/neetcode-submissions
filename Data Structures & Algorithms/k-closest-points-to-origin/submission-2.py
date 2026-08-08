class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0 or k == 0:
            return []
        
        minHeap = []
        heapq.heapify(minHeap)
        
        for point in points:
            x = point[0]
            y = point[1]

            distance = math.sqrt(x**2 + y**2)
            heapq.heappush( minHeap, (distance, point))
        
        res = []
        for i in range(k):
            distance, point = heapq.heappop(minHeap)
            res.append(point)
        
        return res
        





"""
problem:
    - points: 2D array
    - points[i]: [xi, yi] represent coordinate of a point 
    - given an integer: k

    => return k closest point to (0,0)



idea:
    we wanna return k closest points => the min distance to the (0,0) => use minHeap


"""
        