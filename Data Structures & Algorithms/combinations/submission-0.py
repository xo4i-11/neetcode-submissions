class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(start):
            if len(subset) == k:
                res.append(subset.copy())
                return 
            
            for i in range(start, n+1):
                subset.append(i)
                dfs(i+1)

                subset.pop()
        
        dfs(1)

        return res



            
            





"""
return all possible combination => we will use backtracking
- we can imagine a decision tree such that:
    + go left mean choose to include the next node
    + go right mean choose to not include the next node




"""