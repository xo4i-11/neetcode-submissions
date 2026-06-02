class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        
        if len(stones)== 1:
            return stones[0]

        maxHeap=[]
        for stone in stones:
            maxHeap.append(-stone)

        heapq.heapify(maxHeap)


        for stone in stones:
            if len(maxHeap)>1:
                s1 = heapq.heappop(maxHeap)
                s2 = heapq.heappop(maxHeap)

                if s2 > s1:
                    heapq.heappush(maxHeap, -(s2-s1))
            
        if len(maxHeap)==1:
            return abs(maxHeap[0])
        else:
            return 0
    
    