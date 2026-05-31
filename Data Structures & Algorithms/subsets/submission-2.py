class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= [] 
        
        #track the current subset being built subset 
        subset= []

        def dfs(i): #i is the index of the value we are currently at
            #base case, when reaching the leaf node
            # => we already got the subset => append to res
            if i == len(nums):
                res.append(subset.copy())
                return

            #decision to pick nums[i]
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            
            #decision to NOT pick nums[i]
            dfs(i+1)

        
        #starting from idx 0
        dfs(0)
        return res


"""
problem: 
    given array nums of unique int, return all subset of nums

idea: backtracking dfs
    for each number we have 2 choices:
        + don't include it in the current subset
        + include it in the current subset

=> backtracking help us explore both choice: 
+ add the current number -> explore further
+ remvoe it (undo) -> explore without it



                                            []

                          / Include 1                    \ Exclude 1
                       [1]                                []
                 / Include 2 \ Exclude 2          / Include 2 \ Exclude 2
             [1,2]            [1]              [2]             []
          /       \         /      \         /      \        /      \
      +3           -3    +3         -3    +3        -3    +3        -3
 Include 3   Exclude 3 Include 3 Exclude 3 Include 3 Exclude 3 Include 3 Exclude 3
   [1,2,3]     [1,2]    [1,3]      [1]      [2,3]      [2]       [3]        []
"""
        