class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = prev # prev = temp = i-2
            prev = curr # prev = curr = i-1
            curr = max(nums[i] + temp, prev)
        
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

    for i in range(2, len(nums)):
        temp = prev
        prev = curr
        curr = max(temp+ nums[i], curr)
    
    return curr






    

"""
question:
    - nums: array
    - nums[i]: amount of money in ith house
    - cannot rob 2 adj houses

    => return max money we can rob

idea:
    - we use 1 dimension dp
    - if we rob house ith => we are not allow to rob i-1th and i+1th house
    - if we skip house ith => we get the latest value till house ith


array:  5    3   10    10   15   7   20 
dp:     5    5   15    15   30   30  50

we start with elem at idx 0, 1
prev = array[0]
curr = max(array[0], array[1])

for elem at idx i (start at idx 2), we check if:
    max (array[i] + dp[i-2], dp[i-1])

"""

def house_robber_3rd_attempt(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums[0], nums[1])

    prev = nums[0]
    curr = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        temp = prev # prev = temp = i-2
        prev = curr # prev = curr = i-1
        curr = max(nums[i] + temp, prev)
    
    return curr
















































        