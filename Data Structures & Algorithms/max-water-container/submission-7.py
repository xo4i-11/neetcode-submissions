class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0

        while(l<r):
            smaller_edge= min(heights[l],heights[r])
            area=smaller_edge*(r-l)
            res=max(res,area)
            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
         
        return res
            


"""
IDEAS:
#trynna find max area; area= smaller_height.distance

#to maximize the area, we gonna start at 2 side of the array 
=> l=0, r=len(height)-1

#we only move the column with smaller height as the distance gonna be smaller and we wanna preserve the higher col => we will have a chance to have a larger area
(since the more we move the pointer, the smaller the area gonna be)

while moving the ptr, track the largest area


def most_water(height):
    l=0
    r=len(height)-1
    biggest=0

    while l<r:
        area= min(height[l],height[r])*(r-l)
        biggest= max(area,biggest)

        if l<r and height[l]>height[r]:
            r-=1
        elif l<r and height[l]<=height[r]:
            l+=1
    
    return biggest

"""






#the more it come close, the less distance
#if we want to preserve the area or make it to be longer, we need to track of the higher height


    






































