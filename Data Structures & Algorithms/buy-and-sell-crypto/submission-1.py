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


#IDEAS: 2 ptrs

#left=buy,  right=sell 

#set the left to day 1 and the right to day 2

#keep changing the right until reach the end of the prices
#if(buy<sell): we update the profit if its > than the old profit and move the right ptr to keep finding the best profit
#if buy>sell: move the left ptr to the current position of right ptr and keep moving the right ptr by 1 to find the value





#IDEAS:
#2 pointers
# we can use the left ptr to track the buy and right ptr to track the sell


          
        


















































            
    

        


    
        