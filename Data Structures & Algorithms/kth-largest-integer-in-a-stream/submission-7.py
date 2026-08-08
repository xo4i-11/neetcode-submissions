class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]






"""
question:
    add: add elem to the list, then find the kth largest elem (count from 1)

    we wanna keep tracking the kth largest elem => everything that come before 
    the largest kth elem wont matter => what if we use a min_heap and remove all the elem 
    that come before largest kth elem?

    ex: KthLargest(3,[1,2,3,3]) => care about [2,3,3] only and remove 1
    => we always know that the kth largest is arr[0] 



"""
