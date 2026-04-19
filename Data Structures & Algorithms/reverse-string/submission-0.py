class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        Approach:
        using 2 ptr, 1 to track the first idx, 1 use to track the last idx
        loop until l meet r idx in the middle
        during every loop, we swap the left adn right idx 
        """

        l=0
        r=len(s)-1

        while l<r:
            temp=s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1
            r-=1
        return
    

        