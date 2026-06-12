class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        nums.sort()

        def dfs(i):
            #base case
            if i == len(nums):
                res.append(subset.copy())
                return 
            
            # all subset that include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
        
            # all subset that is not include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            dfs(i+1)
        
        dfs(0)
        return res





"""
idea:   
    - ex: [1,2,2,3]
    -   when we decide to skip a 2, we must skip all 2 not to create a duplicate



"""