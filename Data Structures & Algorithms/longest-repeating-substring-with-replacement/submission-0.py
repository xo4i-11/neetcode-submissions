class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string s that has uppercase char
        #int k -> we can choose UP TO (which means <=k) k char of string and replace with another uppercase english char
        #length of longest substring which contains 1 distinct char

        #IDEAS:
        #first, we set the left pointer at 0 and traverse the right ptr from 0 to len(s)
        #every time we move the right pointer, we will track the number of occurance of the char in side it
        
        # for ex: A B A B B A
        #         l     R
        # => A:2 B:2

        #Afterwards, we will check if the len of the current window (for the example is 4: ABAB)
        # minus the smallest occurances gonna exceed the k or not 
        # if subtraction <=k => keep moving the right ptr
        #if not: l+=1  

        count={}
        res=0

        l=0
        for r in range(len(s)):
            
            if (s[r] in count):
                count[s[r]]+=1
            else:
                count[s[r]]=1

            while(r-l+1) - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res

        


