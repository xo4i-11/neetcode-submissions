class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        visited= set()
        time= 0 
        fresh=0

        def addRotten(r,c):
            nonlocal fresh

            #out of bound cell or not valid cell
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or grid[r][c]==0:
                return 
            
            queue.append((r,c))
            visited.add((r,c))
            grid[r][c]=2
            fresh-=1


        #find rotten banana and add to the queue, mark it as visited
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append((r,c))

                elif grid[r][c] == 1:
                    fresh +=1 


        #now, from the rotten banana, we find fresh banana, mark it as rotten, and keep doing bfs
        while queue and fresh >0:
            for i in range(len(queue)):
                r,c = queue.popleft()

                addRotten(r+1,c)
                addRotten(r-1,c)
                addRotten(r,c+1)
                addRotten(r,c-1)

            time +=1
        

        if fresh==0:
            return time
        else:
            return -1
        
        
            
    




"""
problem:
- 2D matrix: grid
- cell:
    + 0 represent empty cell
    + 1 represent fresh fruit
    + 2 represent rotten fruit

if fresh adj to rotten => fresh become rotten

return: min number of mins it takes till there is 0 fresh fruit
        if impossible => return -1


idea: BFS
- first, we need to find all the banana and add it to the queue
- after all the banana in the queue, starting from 1 of it, check the 4 other direction

"""
        