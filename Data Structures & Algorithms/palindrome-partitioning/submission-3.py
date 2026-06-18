class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        part = []

        def dfs(i):
            #base case: if i out of bound => reach leaf => return 
            if i == len(s):
                res.append(part.copy())
                return 
            

            for j in range(i, len(s)):
                if self.isPalin(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)

                    part.pop()
        
        dfs(0)
        return res

    def isPalin(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        
        return True

                




"""
idea: BACKTRACKING 

        aab
        /|\
       a aa aab
       /\  \
      a  ab  b
     /
    b 


from a in i=0, we can choose:  + a (valid), aa (valid), aab (invalid -> stop exploring)
from a in i=1, we can choose:  + a (valid), ab(invalid -> stop exploring)
from 



"""



























