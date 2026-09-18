class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])
        
        max1 = self.helper(nums[1:n])
        max2 = self.helper(nums[0:n-1])
        return max(max1, max2)
    
    
    def helper(self, lst):
        n = len(lst)
        
        if n == 1:
            return lst[0]
        
        if n == 2:
            return max(lst[0], lst[1])
        
        prev = lst[0]
        curr = max(lst[0], lst[1])

        for i in range(2, n):
            temp = prev
            prev = curr
            curr = max(curr, temp + lst[i])
        
        return curr
        




"""
problem:
    -  nums[i]: money of ith house
    - couldn't rob 2 adj house, the last and first house are neigbor (circle)

idea:
    - we can use bottom up DP
    - we can run DP 2 times:
        + 1 include first elem and not include last elem since we cannot rob both first and last house
        + 1 not include first elem and include first elem since we cannot rob both first and last house

    - ex: 3 4 5 6 7 8
        + we run dp on: 3 4 5 6 7
        + we run dp on: 4 5 6 7 8
        => we compare and get the max one
"""





"""
idea:   
    - since nums[0] and nums[n-1] can not exist at the same time since it form a cycle
    => we split into 2 case: rob the first house or skip the first house
    - we run house robber on 2 of them and compare => choose the max


arr:    3 5 10 6 4 2 9
dp:     3 5      
"""


def house_robber_2(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]
     
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    n = len(nums)

    nums1= nums[0:n-1]
    nums2 = nums[1:n]

    money1 = rob_helper(nums1)
    money2 = rob_helper(nums2)

    return max(money1, money2)



def rob_helper(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    # create 2 ptr to respresent the value in dp
    prev = nums[0]
    curr = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        temp = prev
        prev = curr
        curr = max(prev, temp + nums[i])     
    
    return curr


























