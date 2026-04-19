class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro=0
        l=0

        for r in range(1,len(prices)):
            profit= prices[r] - prices[l]
            
            if l<r and profit>0:
                pro+=profit
            
            l+=1

        return pro


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









def best_time(prices):
    l=0
    total=0

    for r in range(1,len(prices)):
        profit=prices[r]-prices[l]

        if profit <= 0:
            l+=1
        
        elif profit > 0:
            total+=profit 
            l+=1
    return total



























def best(prices):
    pro=0
    l=0

    for r in range(1,len(prices)):
        profit= nums[r] - nums[l]
        
        if l<r and profit>0:
            pro+=profit
        
        l+=1

    return pro



















































