class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r= max(piles)
        track= max(piles)

        while l<=r:
            speed = (l+r)//2

            total= 0
            for pile in piles:
                time = math.ceil(pile/speed)
                total+=time 
            
            if total <= h:
                track= min(track, speed)
                r= speed-1
            else:
                l= speed+1
        
        return track










"""
koko eating banana:

"""