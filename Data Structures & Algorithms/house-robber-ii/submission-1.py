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
        + 1 include first elem and not include last elem
        + 1 not include first elem and include first elem

    - ex: 3 4 5 6 7 8
        + we run dp on: 3 4 5 6 7
        + we run dp on: 4 5 6 7 8
        => we compare and get the max one
"""