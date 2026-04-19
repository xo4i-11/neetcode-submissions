class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                skipL=s[l+1:r+1]
                skipR=s[l:r]

                return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            l+=1
            r-=1
        
        return True

    
    
    """
    IDEAS:
    2 pointer, 1 from start and 1 from end 
    loop until 2 ptr meet each other => there will be 2 case
    if 2 elem does not match and k<0 => return False
    if 2 elem does not match but k>=0 just skip that variable
    """

