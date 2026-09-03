class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0] , nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        # sliding the 2 pointer 
        for i in range(2, n):
            temp = prev
            prev = curr
            curr = max(temp + nums[i], curr)
        
        return curr



"""
problem: 
    - nums[i]: amount of money ith house has
    - CANNOT rob 2 adj houses
    - return max money 

idea:
    DP
    - ex:   5 3 10 10 15  7 20 
     dp:    5 5 15 15 30 30 50
    
    => dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 

"""




"""
def rob(self, nums: List[int]) -> int:
        #Bottom Up DP (Tabluation)
        #Time: O(n)
        #Space: O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0] , nums[1])

        dp = [0] * n
        
        #base case for first 2 position
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]

"""



"""
- array: nums     nums[i] represent amoint of money

- the ith house is neighbor of (i-1)th and (i+1)th

- planning to rob money from the house, but cannot rob 2 adj houses 


"""


def house_robber(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    prev = nums[0]
    curr = max(nums[0], nums[1])

    return 


    

        



      



















































        