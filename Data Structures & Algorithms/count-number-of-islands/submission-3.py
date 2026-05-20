class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        rows=len(grid)
        cols=len(grid[0])

        count=0
        visited=set()

        def bfs(r,c):
            queue=deque()
            root_node=(r,c)

            queue.append(root_node)
            visited.add(root_node)

            while queue:
                node= queue.popleft()

                #after pop the node, we need to check if each of its neigbor is valid or not
                positions=[(-1,0), (1,0), (0,1), (0,-1)]

                for position in positions:
                    neighbor_row= node[0] + position[0]
                    neighbor_col= node[1] + position[1]

                    neighbor=(neighbor_row, neighbor_col)


                    if 0<=neighbor_row< rows and 0<=neighbor_col<cols and neighbor not in visited and grid[neighbor_row][neighbor_col]=="1":
                        queue.append(neighbor)
                        visited.add(neighbor)
        


        for r in range(rows):
            for c in range(cols):
                square= grid[r][c]

                if square=="1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        

        return count
        




        


        


    







"""

given a binary matrix that represent 1,0; return the number of island
use visted to track

we loop through every row and col to check if the box = 1:
    if it is = 1:
        do BFS, and the neigbor will be the 4 position
        if could not find any of them => count+=1. 
        make sure to track if the node is visited or not

"""
        