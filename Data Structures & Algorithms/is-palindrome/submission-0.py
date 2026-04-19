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
                ord('0')<= ord(c) <= ord('9'))

     
    


