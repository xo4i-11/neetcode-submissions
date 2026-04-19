class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #we can use the 1st condition to say that we can use binary search (choose the middle value and move left 
        #or right based on the position of target ) in every row and findout the value
        

        #with the 2nd condition, we can choose the middle row, if the target is smaller 
        # than 10 [target=2 for ex] (example on the left), we can move up to the row [1,2,4,8]
        
        ROWS= len(matrix)
        COLS= len(matrix[0])

        top=0 #the top ptr
        bot= ROWS - 1
        while top <= bot:
            row = (top+bot)//2
            
            if target > matrix[row][-1]:
                top= row+1
            elif target < matrix[row][0]:
                bot= row -1
            else:
                break

        if not (top<=bot): #do it to handle the break
            return False
        
        row=(top+bot)//2
        l=0
        r=COLS-1
        while l<=r:
            m=(l+r)//2
            if target > matrix[row][m]:
                l= m+1
            elif target < matrix[row][m]:
                r= m-1 
            else: 
                return True
        
        return False



