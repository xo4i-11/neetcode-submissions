class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows  = len(matrix)
        cols = len(matrix[0])

        t = 0
        b = rows - 1

        while t<=b:
            m = (t+b)//2

            if target > matrix[m][-1]:
                t = m +1
            elif target < matrix[m][0]:
                b = m -1 
            else:
                break 
        
        #handle out of bound 
        if t > b:
            return False
        
        row = (t+b)//2
        l = 0
        r = cols - 1

        while l<=r:
            mid = (l+r)//2

            if matrix[row][mid] > target: 
                r= mid -1
            elif matrix[row][mid] < target:
                l = mid +1
            else:
                return True

        return False






"""
idea: do double binary search
    1. search for row
    2. when we found the row, binary search in that row 



"""
        