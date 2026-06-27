class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0 

        visited = set()

        def bfs(r,c):
            queue =deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            

            while queue:
                r1,c1 = queue.popleft()

                for x,y in directions:
                    neighbor_x = r1 + x
                    neighbor_y= c1 + y

                    neighbor = (neighbor_x,neighbor_y)

                    #out of bound
                    if neighbor_x<0 or neighbor_x>=rows or neighbor_y<0 or neighbor_y>=cols:
                        continue
                    
                    if (neighbor_x, neighbor_y) in visited or grid[neighbor_x][neighbor_y] != "1":
                        continue
                    
                    visited.add(neighbor)
                    queue.append(neighbor)
            
            return 





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        
        return count 
        