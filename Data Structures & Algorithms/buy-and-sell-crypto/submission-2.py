class Solution:
    def maxProfit(self, prices: List[int]) -> int:



#IDEAS: 2 ptrs

#left=buy,  right=sell 

#set the left to day 1 and the right to day 2

#keep changing the right until reach the end of the prices
#if(buy<sell): we update the profit if its > than the old profit and move the right ptr to keep finding the best profit
#if buy>sell: move the left ptr to the current position of right ptr and keep moving the right ptr by 1 to find the value





#IDEAS:
#2 pointers
# we can use the left ptr to track the buy and right ptr to track the sell


          
        







        max_profit=0
        l=0

        for r in range(1,len(prices)):
            while prices[r]-prices[l]<0:
                l+=1
                continue
            
            prof=prices[r]-prices[l]
            max_profit=max(prof,max_profit)

        return max_profit








































            
    

        


    
        