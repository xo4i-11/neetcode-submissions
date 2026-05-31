class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #when there is no stone
        if len(stones)==0:
            return 0
        #when there is 1 stone
        if len(stones)==1:
            return stones[0]
        
        #create a max heap
        nev_stones = []
        for stone in stones:
            nev_stones.append(-stone)
        heapq.heapify(nev_stones)

        while len(nev_stones) > 1:
            first = heapq.heappop(nev_stones)
            second = heapq.heappop(nev_stones)

            #when x<y
            if first < second:
                heapq.heappush(nev_stones, first - second)
        
        if len(nev_stones)>=1:
            return abs(nev_stones[0])
        else:
            return 0




        

        
    



"""
problem:  array: stones
          weight = stones[i]

- at each step, choose 2 heaviest stone:
    + if x = y => destroy
    + if x<y => x is destroyed and y becomes y-x

- continue till there is 1 stone
 => return the weight of last remaining stone
 return 0 if none remaining

idea: use max heap (since we wanna get the heaviest stone) 
    since Python only have heapq which is min heap => we turn all the value to negative
    
    ex: first = -8
        second = -7
"""
        