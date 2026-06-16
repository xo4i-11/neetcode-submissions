class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            # num of stair
        stair_num = len(cost)

        # if only 1 step -> must use it
        if stair_num == 1:
            return cost[0]

        #dp[i] means the min cost to reach stair i
        dp = [0] * stair_num

        # start either on stair 0 or 1
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,stair_num):

            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        

        return min(dp[stair_num-1], dp[stair_num-2])
        