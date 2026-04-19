class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_p=0
        
        while r<len(prices):
            if prices[r]> prices[l]:
                profit= prices[r]-prices[l]
                max_p=max(max_p,profit)
            else:
                l=r
            r+=1

        return max_p

"""          
RECCOMMENDED:

l=0
max_p=0

for r in range(1,len(prices)):
    prof= prices[r]-prices[l]

    if l<r and prof>=0:
        max_p=max(max_p,prof)
    else:
        l=r
return max_p

""" 

#IDEAS: 2 ptrs

#left=buy,  right=sell 

#set the left to day 1 and the right to day 2

#keep changing the right until reach the end of the prices
#if(buy<sell): we update the profit if its > than the old profit and move the right ptr to keep finding the best profit
#if buy>sell: move the left ptr to the current position of right ptr and keep moving the right ptr by 1 to find the value





#IDEAS:
#2 pointers
# we can use the left ptr to track the buy and right ptr to track the sell

"""
        max_profit=0
        l=0

        for r in range(1,len(prices)):
            while prices[r]-prices[l]<0:
                l+=1
                continue
            
            prof=prices[r]-prices[l]
            max_profit=max(prof,max_profit)

        return max_profit



"""


"""
ideas: we gonna use sliding window 
# left ptr start at the start, right ptr start at idx 1 and we gonna start traversing the right ptr

# if we see that the prices[r]-prices[l] < 0 => we should move left ptr to the posiiton of right ptr then move right 
# [10,2,1,5,6,7,1]


def selling_stock(prices):
    l=0
    r=1
    biggest=0

    while r<len(prices):
        profit = prices[r]-prices[l]
        biggest=max(biggest,profit)

        if profit<0:
            l=r
        r+=1
        
    return biggest

        
"""
            





































            
    

        


    
        