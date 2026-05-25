class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows= len(grid)
        cols= len(grid[0])
        visited= set()

        queue = deque()

        def addRoom(r,c):
            # if the cell is out of bound or visited or it is water => return 
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == -1):
                return 
            
            visited.add((r,c))
            queue.append([r,c])
        
        #find all the treasure and add it to the queue
        #also mark them as visited in order not to revisit
        for r in range(rows):
            for c in range(cols):
                # find the treasure cell
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        #BFS from the treasure
        distance= 0
        while queue:
            for i in range(len(queue)):
                r, c =queue.popleft()

                grid[r][c] = distance

                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            
            distance += 1





"""
question:
 - 2d matrix: grid:
    + water: -1 (can not be traverse)
    + treasure: 0
    + land: INF (can be traversed)

=> fill each land with distance to its nearest treasure
    + if cannot reach => remain INF

#we can traverse up, down, left, right
    + 


example:
input: 

[ [INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF] ]

    INF -1   0  INF
    INF INF INF -1
    INF -1  INF -1
    0   -1  INF INF 


idea:
using BFS:
- we gonna start BFS from every treasure, then expand it cocurrently in order to find the min possible distance to every land
- we also have to track visited node to ensure it not gonna revisited the "already shortest distance" node



"""