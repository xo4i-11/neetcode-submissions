class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(start):
            #base case
            if len(subset) == k:
                res.append(subset.copy())
                return 
            
            for num in range(start, n+1):
                if num not in subset:
                    subset.append(num)
                    dfs(num+1)

                    subset.pop()
            
            
        dfs(1)
        return res

        