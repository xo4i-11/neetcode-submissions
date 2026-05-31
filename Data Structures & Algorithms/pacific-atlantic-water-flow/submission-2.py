class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #init 2 queues and 2 visited set
        pacific_queue = deque()
        pacific_visited = set()

        atlantic_queue= deque()
        atlantic_visited= set()

        rows= len(heights)
        cols= len(heights[0])

        #assign all the cell in top border to Pacific
        for i in range(cols):
            pacific_queue.append((0,i))
            pacific_visited.add((0,i))

        #assign all the cell in left border to Pacific
        for j in range(1, rows):
            pacific_queue.append((j,0))
            pacific_visited.add((j,0))
        
        #assign all the cell in right border to Atlantic
        for i in range(rows):
            atlantic_queue.append((i,cols-1))
            atlantic_visited.add((i,cols-1))
        
        #assign all the cell in bottom border to Atlantic
        for j in range(cols-1):
            atlantic_queue.append((rows-1,j))
            atlantic_visited.add((rows-1,j))
        
        
        #do bfs from node in the border (we gonna use it for both pacific and atlantic border node)
        def get_coords(queue, seen):
            visited_coords = set()

            while queue:
                row, col = queue.popleft()

                visited_coords.add((row,col))

                directions= [(0,1), (1,0), (-1,0), (0,-1)]
                for row_offset, col_offset in directions:
                    neighbor_row= row + row_offset
                    neighbor_col = col + col_offset

                    if neighbor_row < 0 or neighbor_row >= rows or neighbor_col < 0 or neighbor_col >= cols or (neighbor_row,neighbor_col) in visited_coords or heights[row][col] > heights[neighbor_row][neighbor_col]:
                        continue
                    
                    visited_coords.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col))
            
            return visited_coords
        

        #we get all the valid coordinate and store is in a set
        pacific_coords = get_coords(pacific_queue, pacific_visited)
        atlantic_coords = get_coords(atlantic_queue, atlantic_visited)

        print("pacific: ", pacific_coords)
        print("atlantic: ", atlantic_coords)

        return list(pacific_coords.intersection(atlantic_coords))




                    
                




        









"""
problem:
    - matrix: heights
    - cell: represent the height of the cell above the sea level
    - top + left border: Pacific Ocean
    - bottom + right: Atlantic Ocean

    - water flow in 4 direction, from a cell to neighbor cell with height <=
    - flow into ocean from cells adj to ocean

    => find all cells such that water can flow from that cell to both Pacific and Atlantic Ocean
    
idea:
    - we can use BFS, exploring the 4 direction to see if it can touch both ocean or not
    - we will use 2 set:
        + 1 contains all elem that can reach the Pacific 
        + 1 contains all elem that can reach the Atlantic 

    -  all of the intersection between those 2 set would be what we need (aka both have Pacific and Atlantic)

approach: 
    -  we will do double BFS, 1 for Pacific and 1 for Atlantic
    - 
"""

    