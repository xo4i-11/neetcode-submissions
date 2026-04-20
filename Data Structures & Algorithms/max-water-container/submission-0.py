class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0

        while(l<r):
            smaller_edge= min(heights[l],heights[r])
            area=smaller_edge*(r-l)
            res=max(res,area)
            if min(heights[l+1],heights[r])*(r-l)>area and l+1<r:
                l+=1
            elif min(heights[l],heights[r-1]*(r-l)>area and l<r-1):
                r-=1
            else:
                l+=1
        return res
            