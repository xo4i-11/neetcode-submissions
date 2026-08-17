class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            #when reaching the end 
            if i == len(nums):
                res.append(subset.copy())
                return 
            
            #include the number 
            subset.append(nums[i])
            dfs(i+1)

            #backtrack
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res 


"""
return all possible subsets of nums


idea:
    - we can choose either to include or exclude that elem
    - we have a decisiton tree and we can traverse



"""


def subsets(nums):
    if len(nums) == 0:
        return []
    
    res = []

    subset = []

    def dfs(i):
        
        # Base case: processed every number
        if i == len(nums):
            res.append(subset.copy())
            return
        
        # Choice 1: include nums[i]
        subset.append(nums[i])
        dfs(i+1)

        # Undo the choice so we can try the other path
        subset.pop()

        # Choice 2: don't include nums[i]
        dfs(i+1)

    
    dfs(0)
    return res




"""


[]  --- [1]


"""



























