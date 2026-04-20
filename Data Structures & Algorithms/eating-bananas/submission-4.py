class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #int array: piles=[int]
        #h is the number of hours we have to eat all the banana

        # eating rate: k

        #return the minimum int k such that you can eat all the banana in h hours
        
        #use math.ceil()
        
        #IDEAS:
        #since the maximum number of k is max(piles):
        #ex: [3,6,7,11] => the maximum speed is 11
        #=> we need to try the speed from 1-> 11 and figure out which will be the smallest possible speed
        #=> use binary search

        l=1
        r=max(piles)
        
        res=r

        while(l<r):
            m= (l+r)//2
            time=0
            for pile in piles:
                time+= math.ceil(pile/m)
            
            if time<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res
            

                



