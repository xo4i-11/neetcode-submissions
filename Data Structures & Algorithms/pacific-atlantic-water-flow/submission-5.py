class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0 or len(heights[0]) == 0:
            return []
        
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()


        def dfs(r, c, visited):
            # out of bound 
            if r<0 or r>= rows or c<0 or c>= cols:
                return 
            
            # visited already
            if (r,c) in visited:
                return 
            
            visited.add((r,c))

            offset =[(1,0), (-1,0), (0,1), (0,-1)]

            for x, y in offset:
                nei_r = r + x
                nei_c = c + y

                #explore if the inward  cell is not visited 
                # or out of bound and bigger than the curr cell

                if 0 <= nei_r < rows and 0<= nei_c < cols and (nei_r, nei_c) not in visited and heights[nei_r][nei_c] >= heights[r][c]:
                    dfs(nei_r, nei_c, visited)

        
        #1. Explore from  PACIFIC-border-nodes:
        # dfs from nodes in left col
        for r in range(rows):
            dfs(r, 0, pacific)
        
        #dfs from nodes in top row
        for c in range(cols):
            dfs(0, c, pacific)
        
        #2. Explore from ATLANTIC-border-nodes:
        # dfs from nodes in right col
        for r in range(rows):
            dfs(r, cols-1, atlantic)
        
        # dfs from nodes in bottom col
        for c in range(cols):
            dfs(rows-1, c, atlantic)
        
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        
        return res



        


        








"""
problem:
    - heights: rectangular island
    - heights[r][c]: heights above sea level

    - Pacific Ocean:  top and left side
    - Atlantic: Bottom and right

    - water flow in 4 direction, from a cell to neighboring cell with heights equal or lower
    water can also flow into the ocean from cells adj to ocean

    => find all cells that water can flow from that to both pacific and atlantic



idea:
    - start from the border cell and move in-ward

"""

















