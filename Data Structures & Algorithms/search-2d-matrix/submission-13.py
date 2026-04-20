class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #we can use the 1st condition to say that we can use binary search (choose the middle value and move left 
        #or right based on the position of target ) in every row and findout the value
        

        #with the 2nd condition, we can choose the middle row, if the target is smaller 
        # than 10 [target=2 for ex] (example 1), we can move up to the row [1,2,4,8]
        
        #binary search for the row
        top = 0
        bottom = len(matrix)-1

        while top<=bottom:
            mid= (top+bottom)//2
            if target> matrix[top][-1]:
                top=mid+1
            elif target < matrix[bottom][0]:
                bottom=mid-1
            else: 
                break
            

        
        row = (top+bottom)//2 #it is actually row = mid
        l=0
        r=len(matrix[0])-1

        while l<=r:
            m = (r+l)//2

            if matrix[row][m] > target:
                r=m-1
            elif matrix[row][m] < target:
                l=m+1
            else:
                return True

        return False
                
            







"""
IDEAS:

array: matrix 
int: target 

row in matrix are sorted in non-descending order
first int of every row > last int of prev row

return True if target in matrix
False otherwise



#apporach:

#we gonna do binary search to find the correct row first:
top=0 and bottom=len(matrix)-1
# we gonna compare target with the row first and last elem:
# if the target < the first elem of the chosen row => bottom=mid-1 (ex: target = 4 for example 1)
# if the target > the last elem of the chosen row => top=mid+1 (ex: target =20 for example 1)
# else, it is the correct row => break

#we gonna check if top<=bottom or not since when target=60 in example 1, the top=mid+1 in the second loop and gonna larget than the bottom
=> return False

# we gonna do another binary search to check if the target is in chosen row or not

"""


def search_2d_matrix(matrix, target):
    #we wanna find the row that possibly have target => use binary search
    top=0
    bottom= len(matrix)-1

    while top<=bottom:
        mid = (bottom+top)//2

        if matrix[mid][-1]<target:
            top=mid+1
        elif matrix[mid][0]>target:
            bottom=mid-1
        else:
            break

        if not (top<=bottom): #handle the case when target is not in matrix (for ex: target=60 in example 1)
            return False
    
    row = (top+bottom)//2 #it is actually row = mid
    l=0
    r=len(matrix[0])-1

    while l<=r:
        m = (r+l)//2

        if matrix[row][m] > target:
            r=m-1
        elif matrix[row][m] < target:
            l=m+1
        else:
            return True

    return False
        


        





"""
each row is sorted in non-decreasing order
first int of every row > last int of prev row

return True of target exist, false otherwise


first we loop through every row to find the row that might contain the target


then, we gonna do the binary search inside the row in order to find the target 

"""


def search_2D_matrix(matrix):
    
    for i in range(len(matrix)):
        row = matrix[i]

        if row[-1]>= target:
            l=0
            r=len(row)-1

            while l<=r:
                mid=(l+r)//2

                if row[mid]<target:
                    l=mid+1
                elif row[mid]>target:
                    r=mid-1
                else:
                    return True
            return False #OPTIONAL

    return False
















































