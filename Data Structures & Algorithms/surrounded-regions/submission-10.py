class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited= set()

        rows = len(board)
        cols = len(board[0])
        
        #dfs used to traverse
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 

            if board[r][c] == "X" or (r,c) in visited:
                return 
            

            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return 


        #start DFS from the border O
        for r in range(rows):
            #left border
            if board[r][0] == "O":
                dfs(r,0)
            #right border
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
        
        for c in range(cols):
            #up boarder
            if board[0][c] == "O":
                dfs(0,c)
            #down boarder
            if board[rows-1][c] == "O":
                dfs(rows-1,c)
        
        #for all of every other O that is not from border
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

        return 

            

"""
Idea: we do DFS

- create a visted set to track all of the visited node
- traverse all border cell:
    + when a border cell is O, do DFS and mark all of the O neighbor as visited
- after all border-connected region are found:
    + if a cell is O and not visited => it must be surrounded => change to X
    + otherwise, leave it the same

"""







"""
problem:
    - connect: horizontal or vertical
    - region: connect every 'O' cell
    - surround: + a region is surround if none 'O' are on the edge of board
                + be enclosed by 'X' cell
    

idea:
    1. Find every O on the border.
    2. DFS from those Os.
    3. Mark them as safe because they are connected to the border.
    4. Go through the whole board:
        + O + not safe → change to X
        + safe O → keep O

"""

def surrounded_regions(board):
    if len(board) == 0 or len(board[0]) == 0:
        return None
    
    rows = len(board)
    cols = len(board[0])

    safe = set()

    def dfs(r,c):
        if r < 0 or r>= rows or c<0 or c>= cols:
            return
        
        if (r,c) in safe or board[r][c] != "O":
            return 
        
        safe.add((r,c))

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

        return 


    #start DFS from the border O
    for r in range(rows):
        #left border
        if board[r][0] == "O":
            dfs(r,0)
        #right border
        if board[r][cols-1] == "O":
            dfs(r,cols-1)
    
    for c in range(cols):
        #up boarder
        if board[0][c] == "O":
            dfs(0,c)
        #down boarder
        if board[rows-1][c] == "O":
            dfs(rows-1,c)

    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r,c) not in safe:
                board[r][c] = 'X'
                
    return board


    






    


















        
