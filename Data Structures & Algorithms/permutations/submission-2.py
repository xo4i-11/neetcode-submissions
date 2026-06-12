class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs():
            # stopping case
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 
            
            for num in nums:
                if num not in subset:
                    subset.append(num)
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
        