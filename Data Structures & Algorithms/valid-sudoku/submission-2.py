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
                    board[r][c] in squares[(r//3, c//3)]):     # check if it have duplicate in row or col or square. the key have to be a tuple since it is immutable (r//3,c//3)
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True




#IDEAS:

#to check the row, just loop through every row
#to check the col, loop through every col
#check dup-> use set
#=>use the hashmap with the key is the nunber of row or col, the value is the number in the small blk

#we gonna split it into 9 3x3 squares
#find the coordinate of each square
#for example, we want to set the idx of the square to 0,1,2 
#check dup-> use set
#=>use the hashmap with the key is the tuple(since list cannot be a key due to mutable) contain the cordinate of the big square (0 or 1 or 2) and the value store the number in the small blk

"""

cols=defaultdict(set) #ex: cols[1] = {'3', '9', '6'}
rows=defaultdict(set) # example: rows[0] = {'5', '3', '7'}
squares=defaultdict(set) #ex: square[(0, 1)] = {'1', '5', '9'}, key is a tuple 

for r in range(9):
    for c in range(9):
        if board[r][c]==".":
            continue
        if (board[r][c] in rows[r] or
            board[r][c] in cols[c] or
            board[r][c] in square[r//3,c//3]):
            return False
        
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squares[(r//3,c//3)].add(board[r][c])
    
    return True

"""






























































