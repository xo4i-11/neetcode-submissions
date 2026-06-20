class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i, curr_sum):
            # base case: add to the res when total = target
            if curr_sum == target:
                res.append(subset.copy())
                return 
            
            #base case: stop when reaching the leaf or exceed the sum
            if curr_sum > target or i == len(nums):
                return 
            
            #otherwise, we can either choose to include or not include nums[i]
            subset.append(nums[i])
            dfs(i, curr_sum + nums[i])

            #pop, backtrack
            subset.pop()

            #explore next num (the next idx) aka skip nums[i]
            dfs(i+1, curr_sum)

        
        dfs(0,0)
        return res










"""
idea:
    choose itself or choose next val




"""
        