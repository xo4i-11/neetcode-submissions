class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        candidates.sort()
        subset=[]

        def backtrack(i, total):
            if total == target:
                res.append(subset.copy())
                return 
            
            if total > target or i == len(candidates):
                return
            
            #pick candidates[i]
            subset.append(candidates[i])
            backtrack(i+1,total + candidates[i])

            #back track
            subset.pop()

            #skipping candidates[i] + prevent duplicate
            #ex: [1,1,1,2]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, total)


        backtrack(0,0)

        return res



"""
problem:
     - given an array of int: candidates (may contain dup)
     - int: target
    
    each elem from candidates may be chosen at most once within a combination



idea:
    - use back tracking
    - we use dfs in a decision tree:
        + 1 option is to include nums[i]
        + 1 option is to exclude nums[i]
    
    - since it may still contain duplicate:
        + ex: [10, 1, 2, 7, 6, 1]   target = 8 
            there might be combination:
                * [1,7] (first "1" and "7")
                * [7,1] ("7" and second "1")

    - to prevent the above, we sort them and skip the duplicate elem:
        + ex: [1, 1, 2, 6, 7, 10] target = 8 
            => we will work with the first "1" and skip the second "1"
"""