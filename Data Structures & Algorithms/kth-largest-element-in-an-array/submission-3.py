class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        
        for num in nums:
            heapq.heappush(minHeap,num)
        
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
        


"""
problem:    
    - unsorted array: nums
    - int: k
    => return kth largest elem
    

idea:
    - use min heap and only keep the k largest number so far in the minHeap



"""
        