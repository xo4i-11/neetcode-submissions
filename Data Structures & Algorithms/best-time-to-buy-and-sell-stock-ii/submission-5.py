class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit=0 
        l=0

        for r in range(1,len(prices)):
            profit = prices[r]-prices[l]
            if profit > 0:
                total_profit+=profit
            l+=1
        
        return total_profit

"""
BETTER SOLUTION

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit=0 

        for i in range(1,len(prices)):
            profit = prices[i]-prices[i-1]
            if profit > 0:
                total_profit+=profit
        
        return total_profit

"""
                
"""
    IDEAS: 
    Basically, we buy low, sell high
    => if profit >0, we gonna add it to the total_profit 
"""










"""""
        *                   *
                    *               
            *                    *



here is the graph represent the changing in stock price
we could buy and sell multiple time, not just one
=> the easiest way is whenever we see the price increase, we calcuatle the diff and just add it to the oversall sum

"""""

































