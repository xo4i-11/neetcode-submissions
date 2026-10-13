class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(l,r):
            track = 0
            while l>=0 and r< len(s) and s[l] == s[r]:
                l-=1
                r+=1
                track +=1
            
            return track
            
            
        
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            count += odd + even
        
        return count







"""
idea:
    - we loop through every single char
    - we expand from 2 side





"""
        