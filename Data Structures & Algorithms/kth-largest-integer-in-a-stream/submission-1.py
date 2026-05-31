class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #min heap with k largest int
            self.min_heap = nums 
            self.k = k

            #only store k largest elem in the heap, since we dont need to care ab smaller elem
            heapq.heapify(self.min_heap)
            while len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        
        #remove if the min heap have more than k elem 
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]        



"""
problem:
    + Design a class to find the kth largest int in a stream of values, include duplicate
    
- constructor: init the object, given an int k and stream int nums
- add: add elem to the stream, return the kth largest elem

idea: using min heap

- min heap: + add (push) elem in log(n) time
            + pop elem in log(n) time
            + get min uin O(1) time

- use min heap because when we add el
"""