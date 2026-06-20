class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 
            
            #explore 
            for i in range(len(nums)):
                if nums[i] not in subset:
                    # since we must include every num
                    subset.append(nums[i])
                    dfs()

                    subset.pop()
                
                
        dfs()
        return res






"""
problem:
    - find all the permutation

idea:
    - we use dfs + backtracking 
    - we only add to the res only if the len(susbet) == len(nums)
    
    - when traversing, we check that number + include all the neighbor (using a loop)



"""
        