class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_island = 0
        visited = set()
        
        #the point is to return the count represent number of node 
        def dfs(r,c):
            #base case
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0

            #base case: visited or not =1
            if grid[r][c] == 0 or (r,c) in visited:
                return 0 

            visited.add((r,c))

            count = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

            return count 
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_island = max(dfs(r,c), max_island)
        
        return max_island





###################################
def max_area(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_area = 0
    visited = set()

    def dfs(r, c):
        nonlocal area

        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == 0 or
            (r, c) in visited
        ):
            return

        visited.add((r, c))
        area += 1

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

        return 



    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                area = 0
                dfs(r,c)
                max_area = max(area, max_area)
    
    return 