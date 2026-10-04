class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left, right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            
            return s[left+1 : right]

        longest = ""

        for i in range(len(s)):
            #odd length
            odd = expand(i,i)

            #even length
            even = expand(i,i+1)

            if len(odd) > len(longest):
                longest = odd
            
            if len(even) > len(longest):
                longest = even
        
        return longest












"""
idea:
    loop through every char inside a word, there will be 2 case, which are 



"""






















        
    







"""
idea:   
- using 2 ptr
- instead of checking every substring, we start from the middle and expand it to the 
2 side to see if it's substring or not

"""

def longest_palindrome(s):
    
    longest = ""

    def expand(l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1

        return s[l+1:r] 

    for i in range(len(s)):
        # handle odd # of char
        odd = expand(i,i)
        
        #handle even # of char
        even = expand(i,i+1)

        if len(odd) > len(longest):
            longest = odd
        
        if len(even) > len(longest):
            longest = even
    
    return longest



