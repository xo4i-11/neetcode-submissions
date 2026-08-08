class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #base case
        if len(stones) == 0:
            return 0
        
        if len(stones) == 1:
            return stones[0]

        new_stones = []
        for stone in stones:
            new_stones.append(-stone)
        
        print(new_stones)

        heapq.heapify(new_stones)

        while len(new_stones) >= 2:
            stone1 = heapq.heappop(new_stones)
            stone2 = heapq.heappop(new_stones)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(new_stones, stone1 - stone2)
        
        if len(new_stones) == 1:
            return abs(new_stones[0])
        else:
            return 0

    

        
    





"""
question:
    - stones: array
    - stones[i]: weight of ith stone

    - at each step:
        + choose 2 heaviest stone with weight x,y:
            * if x = y => both destroyed (both being removed from the lst)
            * if x < y => x is destroyed, y_new_weight  = y-x
            => continue till there is <= 1 stone 
    
    return weight of last remaining stone 
    or return 0 if none remain

idea:
    - since we need 2 heaviest stone => we will use max heap
"""
        