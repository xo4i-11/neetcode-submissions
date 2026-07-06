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
- using 2 ptr
- instead of checking every substring, we start from the middle and expand it to the 
2 side to see if it's substring or not

"""