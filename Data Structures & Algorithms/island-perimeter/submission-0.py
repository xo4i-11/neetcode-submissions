class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #bfs
        rows=len(grid)
        cols=len(grid[0])
        visited=set()

        #what we wanna return: the perimeter => we need to count the number of square
        def dfs(r,c):
            #base case: out of bound
            if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0:  
                return 1 
            
            #base case: water -> edge
            if grid[r][c]==0:
                return 1
            
            if (r,c) in visited:
                return 0
            
            #otherwise, it is land and we can recursively add the perimeter of the 4 neighbor
            visited.add( (r,c) )  
            perimeter= dfs(r,c+1) + dfs(r+1,c) +dfs(r-1,c) + dfs(r,c-1)
            return perimeter

            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)
        
        return 0
            





"""
idea: use DFS 
 - guarantee to have 1 island.
 - we create a visited to track the visited node
 - we DFS the 4 neighbors of a node until there is no island left (make sure never dfs the node that is already in visited)



"""