class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit=0 

        for i in range(1,len(prices)):
            profit = prices[i]-prices[i-1]
            if profit > 0:
                total_profit+=profit
        
        return total_profit

                
    """
    IDEAS: 
    Technique: Shrinking Sliding Window

    I still set the left and right ptr at the idx 0 and traverse the right pointer 

    immediately sell on the same day if prices keep decreasing. For example: [4,3,2,1] => return 0 => we could run the right ptr from 0 to check (dont worry)


    profit =0

    for r in range(len(nums)):
    


    return max_profit
            

    """