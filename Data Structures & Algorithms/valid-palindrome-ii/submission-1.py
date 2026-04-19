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

    loop until 2 ptr meet each other => there will be 2 case:

    1.if it is the same, then just keep moving the ptr

    2.if it is not the same, there will be 2 case:
    - we need to move pointer left by 1, after that, we will check the remaining palindrome if it is correct or not by comparing it wil its reverse
    

    """

