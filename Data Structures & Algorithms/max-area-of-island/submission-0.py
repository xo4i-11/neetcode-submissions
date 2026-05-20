class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited= set()
        max_island= 0

        rows= len(grid)
        cols= len(grid[0])


        def dfs(r,c):
            #base case, when it meet the water, or out of bound, return 0
            if r >= rows or c>= cols or r<0 or c<0 :
                return 0
            
            if grid[r][c]==0 or (r,c) in visited:
                return 0
            

            visited.add((r,c))
            
            count = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

            return count
            
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==1:
                    max_island= max(max_island, dfs(r,c))
        
        return max_island










"""
problem:   
- given grid, each block = 0 or = 1

=> count the max area island 

idea:
    use DFS, track the number of island, return the max

    - first, we create a visited class to ensure it does not revisit node
    - when we meet the land (1), we dfs the 4 neighbor until it meet water and count not explore anymore
    - 
"""
        