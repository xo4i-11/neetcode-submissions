class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        l=0
        max_profit = 0

        for r in range(len(prices)):
            diff = prices[r] - prices[l]
            max_profit= max(max_profit, diff)

            if diff < 0:
                l=r


        return max_profit
        