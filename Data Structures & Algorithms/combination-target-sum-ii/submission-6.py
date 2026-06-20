class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        
        #when do dfs, there will be 2 decision:  
        # include or skip
        def dfs(i, curr_sum):
            #base case
            if curr_sum == target:
                res.append(subset.copy())
                return 

            if curr_sum > target or i == len(candidates):
                return 
            
            for j in range(i, len(candidates)):
                #skip duplicate
                if j > i and candidates[j] == candidates[j-1]:
                    continue 
                
                subset.append(candidates[j])
                dfs(j + 1, curr_sum + candidates[j])
                subset.pop()

        dfs(0, 0)
        return res



        dfs(0,0)
        return res



"""
problem:
     - given an array of int: candidates (may contain dup)
     - int: target
    
    each elem from candidates may be chosen at most once within a combination



idea:
    - use back tracking
    - we use dfs in a decision tree:
        + 1 option is to include(candidates[i]
        + 1 option is to exclude(candidates[i]
    
    - since it may still contain duplicate:
        + ex: [10, 1, 2, 7, 6, 1]   target = 8 
            there might be combination:
                * [1,7] (first "1" and "7")
                * [7,1] ("7" and second "1")

    - to prevent the above, we sort them and skip the duplicate elem:
        + ex: [1, 1, 2, 6, 7, 10] target = 8 
            => we will work with the first "1" and skip the second "1"
"""



"""
def combination(candidates, target):

    # sort so duplicates are adjacent
        candidates.sort()

        res = []
        subset = []

        def backtrack(start, curr_sum):

            # found a valid combination
            if curr_sum == target:
                res.append(subset.copy())
                return

            # exceeded target
            if curr_sum > target:
                return

            # try every possible choice starting from start
            for i in range(start, len(candidates)):

                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # choose
                subset.append(candidates[i])

                # move to i+1 because each number
                # can only be used ONCE
                backtrack(i + 1, curr_sum + candidates[i])

                # undo choice
                subset.pop()

        backtrack(0, 0)

        return res
        



"""
















