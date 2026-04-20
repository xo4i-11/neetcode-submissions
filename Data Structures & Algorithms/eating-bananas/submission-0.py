class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #int array: piles=[int]
        #h is the number of hours we have to eat all the banana

        # eating rate: k

        #return the minimum int k such that you can eat all the banana in h hours
        
        #might use ceil: for ex: math.ceil(1:2)=1 => can calculate the hours that was use

        for k in range (1,max(piles)+1):
            total=0
            for pile in piles:
                total+=math.ceil(pile/k)
            
            if(total<= h):
                return k
        return 0
