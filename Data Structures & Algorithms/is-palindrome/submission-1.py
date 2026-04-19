class Solution:
    def isPalindrome(self, s: str) -> bool:
        #idea:
        # we create an left ptr and right ptr and move it until they meet each other
        #whenever a pointer meet a space, it has to +1
        #keep adding up by 1 to the 2 pointers until they meet
        left_ptr=0
        right_ptr=len(s)-1

        while(left_ptr < right_ptr):
            while (left_ptr< right_ptr and not self.alphaNum(s[left_ptr])):
                left_ptr+=1
            while (right_ptr>left_ptr and not self.alphaNum(s[right_ptr])):
                right_ptr-=1
            
            if(s[left_ptr].lower() != s[right_ptr].lower()):
                return False
            
            left_ptr+=1
            right_ptr-=1

        return True
        
        
    def alphaNum(self,c):
        return (ord('A')<= ord(c) <= ord('Z') or 
                ord('a')<= ord(c) <= ord('z') or 
                ord('0')<= ord(c) <= ord('9')) #make sure that '0' but not 0

     
    

"""
#IDEAS:

l=0
r=len(s)-1

while (l<r):
    while l<r and not s[l].isalnum():
        l+=1
    while l<r and not s[r].isalnum():
        r-=1
    
    if s[l].lower() != s[r].lower():
        return False
    else:
        l+=1
        r-=1
return True









#create a function to to validate the char

def alpha_num(c):
    if ord('a')<=ord(c)<=ord('z'):
        return True
    if ord('0')<=ord(c)<=ord('9'):
        return True
    if ord('A')<=ord(c)<=ord('Z'):
        return True
    return False


def palindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        while l<r and self.alpha_num(s[l])==False:
            l+=1
        while l<r and self.alpha_num(s[r])==False:
            r-=1
        
        if s[l].lower()!=s[r].lower():
            return False
        
        l+=1
        r-=1
    
    return True

"""



























































































































