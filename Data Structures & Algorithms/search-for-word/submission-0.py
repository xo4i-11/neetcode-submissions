class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        #track the visited word in the path
        visited = set()

        check = [False]

        # r,c to track the position in the board
        # i is to track the current char in the word
        def dfs(r,c,i):
            # if reach the last char of the word
            if i == len(word):
                check[0] = True
                return 
            
            # if out of bound
            if r <0 or r>=rows or c<0 or c>=cols:
                return 
            
            # if char in word is not in board[r][c] or row, col already been visited
            if word[i] != board[r][c] or (r,c) in visited:
                return 
            
            visited.add((r,c))

            dfs(r,c-1,i+1) 
            dfs(r,c+1,i+1)
            dfs(r-1,c,i+1)
            dfs(r+1,c,i+1)

            visited.remove((r,c))
            return
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,0)
            
        return check [0] 









        





"""
idea:
    - a word can be form horizontally or vertically
    => dist = [(-1,0), (1,0), (0,-1), (0,1)]
    

    brute force: backtracking
    we start from a char, check the 4 direction and keep exploring from those neigbor

"""