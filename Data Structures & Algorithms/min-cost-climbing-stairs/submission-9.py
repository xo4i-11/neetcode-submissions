class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0   # dp[i-2]
        curr = 0   # dp[i-1]

        for i in range(2, len(cost) + 1):
            next_cost = min(
                cost[i - 2] + prev,
                cost[i - 1] + curr
            )

            prev = curr
            curr = next_cost

        return curr
        
        





"""
problem: 
- given a list: cost
- cost[i] = cost to take step from ith floor
- from ith floor, we can choose to go to (i+1)th floor or (i+2)th floor
- we reach the top of the stair case when we past the last index in cost

=> find the min cost to reach the top

idea:
- bottom up DP, since the current cost relies on the prev 2 cost
"""


"""
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        #the dp array must have the len of n+1 since it must past the last elem to reach the top
        dp = [0]*(n+1)

        # the cost of first 2 steps are 0, we start iterate from i=2 -> n+1
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]


"""





"""
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

"""









"""
prob:
    - cost: array of int
    - cost[i]: cost for taking step from ith floor
    - when pay the cost, we can step either: (i+1)th floor or (i+2)th floor
    - we can choose to start at idx 0 or 1

    - return min cost to past the last idx


idea:
    - cost to start at step 1: 0
    - cost to start at step 2: 0

    - the step 3 will depends on how you did in step 1 and 2
    - we gotta choose the min between (1, 2)

    
"""

def min_cost(cost):
    if len(cost) == 0:
        return 0
    
    if len(cost) == 1:
        return cost[0]

    if len(cost) == 2:
        return min(cost[0], cost[1])
    
    prev = 0
    curr = 0

    for i in range(2, len(cost) + 1):
        temp = prev
        prev = curr
        curr = max(min(temp + cost[i]), curr)









def min_cost(cost):
    if len(cost) == 0:
        return 0
    
    if len(cost) == 1:
        return cost[0]
    
    if len(cost) == 2:
        return min(cost[0], cost[1])

    
    









































        