class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #IDEAS:
        #for 1st condition, we wanna make sure each row dont contain any duplicates -> use the set, add all the elem and check if a elem is duppilcate or not
        #for 2nd condition, we do the same as above

        #Use hashmap 
        #+) key store the cordinate of the 3x3 box
        #+) value store a set which represent the cordinate of square inside the box, we use set to check if there is duplicate or no


        cols=defaultdict(set) #create the set with the default value is the set 
        rows=defaultdict(set)
        squares=defaultdict(set) #key =(row//3, col//3) => this gonna split into 3 squares with idxs of 0,1,2 respectively

        for r in range(9):
            for c in range(9):
                if board[r][c]==".": #if the small square is empty
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[r//3, c//3]):     # check if it have duplicate in row or col or square
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        
        return True
