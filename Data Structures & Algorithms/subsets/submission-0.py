class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= [] 

        subset= []
        def dfs(i): #i is the index of the value we are currently at
            if i >= len(nums):
                res.append(subset.copy())
                return

            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res


"""
problem: 
    given array nums of unique int, return all subset of nums

idea: backtracking dfs

"""
        