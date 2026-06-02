class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        heapq.heapify(minHeap)
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (distance, [x,y]))

        res=[]
        for i in range(k):
            distance, point = heapq.heappop(minHeap)
            res.append(point)

        return res        









"""
question:
    given array: points
    int: k represent the k closest point to (0,0)

    return k closest point to (0,0)

idea:
    return k closest point => we only need to handle k point => store it in a min heap, get it by heappop
    - we loop through every point and compute the distance to (0,0) then add to a min heap
    - 




"""