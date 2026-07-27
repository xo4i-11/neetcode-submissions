class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 0 or h == 0:
            return 0

        l = 1
        r  = max(piles)
        
        #the "always valid speed" is the max speed 
        min_speed = r 

        
        while l<=r:
            # eating speed 
            m = (l+r)//2

            time_total = 0 
            #test out that eating speed to check if its min or not
            for p in piles:
                time_total += math.ceil(p/m)
            
            if time_total > h:
                l = m + 1
            elif time_total <= h:
                min_speed = min(min_speed, m)
                r = m-1

        return min_speed



        

        




"""
idea:   do a binary search in a list that store all of the possible speedm
        we gonna find the min speed apossible



"""
        

        