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

            while(l<=r):
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
            

                









"""
int array: piles = []
number of banana in pile ith: piles[i]
int, number of hours we need to eat all the bananas: h
eating rate: k

if less than k bananas => finish eating the pile but cannot go to another pile


#pattern:
if k is small -> koko eating slow -> too many hours
if k is large -> koko eating faster -> less hours
=> 1<=k<=max(piles)

It follow monotonic behavior (moving in a way, either decrease or increase) => we should use binary search
for example: 
k:   1   2   3   4   5   6   7
ok:  F   F   F   T   T   T   T 
=> once it is true at 4, it gonna true for all the things after 4 (like 5,6,7,8)


# BINARY SEACH IS BASE ON EATING SPEED (K), NOT BASE ON THE ARRAY.=> l=1, r=max(piles)
# AND 1<=K<=MAX(PILES) 

Apporach:
we gonna use binary search.
instead of doing binary search inside the array, we imagine there is an array that start from 1-> max(piles) that represents the eating speed k (1<=k<=max(piles))

l=1,r=max(piles)
we gonna create a variable to track the smallest possible variable k: res=r (r=max(piles) will always a correct answer but we need to find the smallest possible)

we gonna loop such that l<=r and find the mid=(l+r)/2
we gonna create a variable to find the hour of eating when k=mid
    inside that loop, we gonna loop through every element of piles to find the total time of eating with the speed of: k=mid
    if time<=h => res=mid and r=mid-1 
    if time>h => l=mid+1

"""

def koko_eating_banana(piles,h):
    #possible eating speed run from 1-> max(piles)
    l=1
    r=max(piles)
    res=r

    while l<=r:
        mid=(l+r)//2
        
        mid_time=0

        for pile in piles:
            mid_time+= math.ceil(float(pile)/mid)
        
        if mid_time>h:
            l= mid+1
        else:
            res=min(res,mid)
            r=mid-1
            
    return res







#elem in the piles is the number of banana for each pile
#we trynna find the eating speed

# we know that if the eating speed equals to the maximum number of banana in the piles => it always true
#ex: 1  2  3  4  5  6  7 
#    F  F  F  F  T  T  T
# we will trynna find the number 4 => use binary search
#

def koko_eating_banana(piles,h):
    l=1
    r= max(piles)
    res=r

    while l<=r:
        mid = (l+r)//2
        total_time=0
        for num in piles:
            time= math.ceil(num/mid)
            total_time+=time
        if total_time >h:
            l=mid+1
        else:
            res=min(res,total_time)
            r=mid-1
        


    






















    



    































