class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k == 0:
            return None
        
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]




"""
problem:
    - nums: unsorted array
    - k: int
    => return kth largest elem in array

idea:
    since we need the kth largest elem, we only need to keep k element and can 
    remove all the elem that come before the kth largest elem
    => we can use minHeap
"""
        