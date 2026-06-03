class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # store all combination
        res = []

        #current combination being built
        subset = []

        def backtrack(i, curr_sum):
            #base case: if found the target
            if curr_sum == target:
                res.append(subset.copy())
                return 
            
            #base case: if exceed the target or reach the leaf
            if curr_sum > target or i == len(nums):
                return
            
            #choice 1: include nums[i]
            subset.append(nums[i])
            backtrack(i, curr_sum + nums[i])

            #undo the choice
            subset.pop()

            #choice 2: skip nums[i] (not choosing)
            backtrack(i+1, curr_sum)

        backtrack(0,0)
        return res 










"""
Problem: 
    -  array of distinct int: nums
    - int: target

=> return a list of unique combination of number that sum = target
 - 1 number can be used unlimited time


idea: using backtracking
 - think about a tree 
 
"""

