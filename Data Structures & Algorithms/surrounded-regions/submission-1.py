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

            




        
