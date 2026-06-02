class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=[]
        for num in nums:
            maxHeap.append(-num)
        
        heapq.heapify(maxHeap)
        
        i=0
        while i<k:
            num = heapq.heappop(maxHeap)
            i+=1
            if i == k:
                return -num
        

        



            
            
        





"""
problem:    
    - unsorted array: nums
    - int: k
    => return kth largest elem
    

idea:
    - use max heap




"""
        