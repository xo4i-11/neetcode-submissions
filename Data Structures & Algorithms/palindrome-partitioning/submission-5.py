class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        subset = []

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i, len(s)):
                if self.is_palin(i,j,s): 
                    subset.append(s[i:j+1])
                    dfs(j+1)

                    subset.pop()
        
        dfs(0)
        return res


    def is_palin(self,l,r,s):
        while l<r:
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        return True





"""
            aab
        /    |    \

      a|ab  aa|b   aab|
      /       |  
 a|a|b       aa|b| 


"""




"""
s = "aab"

0  1  2 
a  a  b


0 1 2 3 4 5 6
a a b b c c d


a|abbccd => we gotta find palindrome in the right half
+ a|bbccd


aa|bbccd =>
aab|bccd



"""