class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        right =1
        max_p=0

        while(right< len(prices)):
            if(prices[left]<prices[right]):
                profit =prices[right]-prices[left]
                if(profit>max_p):
                    max_p=profit
        
            else:
                left=right
        
            right+=1
    
        return max_p


#IDEAS: 2 ptrs

#left=buy,  right=sell 

#set the left to day 1 and the right to day 2

#keep changing the right until reach the end of the prices
#if(buy<sell): we update the profit if its > than the old profit and move the right ptr to keep finding the best profit
#if buy>sell: move the left ptr to the current position of right ptr and keep moving the right ptr by 1 to find the value



    

            
    

        


    
        