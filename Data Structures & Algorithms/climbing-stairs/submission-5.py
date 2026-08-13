class Solution:
    def climbStairs(self, n: int) -> int: 
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        #number of way to reach prev step (step 1)
        prev = 1 

        # number of way to reach curr step (step 2)
        curr = 2

        #loop from 3 -> n
        for i in range(2, n):
            temp = prev
            prev = curr
            curr = curr + temp
        
        return curr
        


        



"""
problem:
    - number of step: n
    - climb either 1 or 2 steps at a time

    => return number of distinct ways to climb


idea:
    using DP memoization (cache) since there will be duplicate sum.
    - we will do bottom up DP, starting from step 1, 2 and go to next step
    - we can see that for each step, the number of way depends on the prev 2 steps 
    
        
"""





def climb(n):
    if n <= 2:
        return n
    
    prev = 1
    curr = 2

    for i in range(2, n):
        temp = prev
        prev = curr
        curr = temp + curr
    
    return curr






"""
the first and the second step is always the base case
for the third step, it will depends on the first second
the third = first + second

=> climbing_stair(n) = climbing_stair(n-1) + climbing_stair(n-2)


"""
def climbing_stair(n):
    if n <= 2:
        return n
    
    prev = 1
    curr = 2

    for i in range(2, n):
        temp = prev
        prev = curr
        curr = temp + curr
    
    return curr

    






































        