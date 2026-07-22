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

            # clean up that elem if we dont go in that path
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




def word_search(board, word):
    rows = len(board)
    cols = len(board[0])

    visited = set() 
    check = [False]

    def dfs(r,c,i):
        #meet every char => found the word
        if i == len(word):
            check[0] = True
            return 

        #base case: out of bound
        if r<0 or r>=rows or c<0 or c>=cols:
            return 
        
        # base case: if visted or not the right char
        if word[i] != board[r][c] or (r,c) in visited:
            return 
        
        visited.add((r,c))

        #explore 4 direction
        dfs(r-1, c, i+1)
        dfs(r+1, c, i+1)
        dfs(r, c+1, i+1)
        dfs(r, c-1, i+1)

        #backtrack
        visited.remove((r,c))

        return 



    for r in range(rows):
        for c in range(cols):
            dfs(r,c,0)

    return check[0]








def word_search_attempt_2(board, word):
    rows = len(board)
    cols = len(board[0])

    check = False
    visited = set()

    def dfs(r,c,i):
        nonlocal check

        if check == True:
            return 

        if i == len(word):
            check= True
            return 
        
        #out of bound
        if r<0 or r>=rows or c<0 or c>=cols:
            return 
        
        #if visited or different
        if (r,c) in visited or board[r][c] != word[i]:
            return 
        
        visited.add((r,c))

        #explore 4 direction
        dfs(r+1,c,i+1)
        dfs(r-1,c,i+1)
        dfs(r,c+1,i+1)
        dfs(r,c-1,i+1)

        #backtrack
        visited.remove((r,c))

    for r in range(rows):
        for c in range(cols):
            dfs(r,c,0)
    return check 
        
            
















"""
idea:   backtracking 
    loop through every char until find the first character in word
    from that, we start exploring 4 direction, backtracking when go into a wrong direction


"""





def word_search(board, word):
    check = False
    seen = set()

    rows = len(board)
    cols = len(board[0])

    def dfs(r,c,i):
        nonlocal check

        if check == True:
            return 
        
        #found the last char in word
        if i == len(word):
            check = True
            return 

        #base case: out of bound
        if r>= rows or r<0 or c >= cols or c< 0:
            return

        #if already visited or not the right char:
        if (r,c) in seen or board[r][c] != word[i]:
            return 
        
        seen.add((r,c))

        dfs(r+1, c, i+1)
        dfs(r-1,c,i+1)
        dfs(r,c+1, i+1)
        dfs(r, c-1, i+1)

        seen.remove((r,c))

    for r in range(rows):
        for c in range(cols):
            dfs(r,c,0)
    
    return check




















