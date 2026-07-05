class Solution:
    def climbStairs(self, n: int) -> int: 
        if n <= 2:
            return n 
        
        a = 1
        b = 1

        for i in range(n-1):
            temp = a
            a = a + b 
            b = temp
        
        return a

        



"""
problem:
    - number of step: n
    - climb either 1 or 2 steps at a time

    => return number of distinct ways to climb


idea:
    using DP memoization (cache) since there will be duplicate sum.
    
    - we will start from the last step: n
    - at any step, the number of ways depend on the next 2 steps (we start from step n):
        + ex: in the example below, step 2 depends on step 3 and 4 

    => we start from the last 2 step, let it be a,b and each of it have 1 way to reach step n
    - we shift it by 1 every time until a reach step 0 => that is our result
    

    ex n=5:
        - at step 5, we have 1 way to reach 5
        - at step 4, we have 1 way to reach 5
        - at step 3, we have 2 ways to reach 5 (step 4 + step 5)
        - at step 2, we have 3 ways to reach 5 (step 3 + step 4)
        - at step 1, we have 5 ways to reach 5 (step 2 + step 3)
        - at step 0, we have 8 ways to reach 5 (step 1 + step 2)
        
"""


        