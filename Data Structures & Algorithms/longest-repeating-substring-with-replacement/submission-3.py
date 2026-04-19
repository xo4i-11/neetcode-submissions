class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string s that has uppercase char
        #int k -> we can choose UP TO (which means <=k) k char of string and replace with another uppercase english char
        #length of longest substring which contains 1 distinct char

        #IDEAS:
        #first, we set the left pointer at 0 and traverse the right ptr from 0 to len(s)
        #every time we move the right pointer, we will track the number of occurance of the char between the 2 ptrs
        
        # for ex: A B A B B A
        #         l     R
        # => A:2 B:2

        #Afterwards, we will check if the len of the current window (for the example is 4: ABAB)
        # minus the highest occurances gonna exceed the k or not 
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

            while(r-l+1) - max(count.values())>k: #r-l+1 is the length of the current window 
                count[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res

        


#string s consist of uppercase english char
#an integer k
# can choose up to k char 

#thinking of using fast slow ptrs

    


"""
IDEAS:
we wanna find the length of the longest possible substring after replacement
=> use sliding window 

l=0,r=0 
we gonna loop the right pointer until reaching the end of the string

every time looping through the string, 
we gonna track the character's occurance between the 2 ptr to see if its gonna create a substring that would be longest after k replacement 
and only stop when the substring is not a substring.

after that, we will do l+=1 to find another substring 

while traversing, we need to track the longest streak
"""

def longest_repeating(s,k):
    l=0
    streak=0
    count={}

    for r in range(len(s)):
        if s[r] in count:
            count[s[r]]+=1
        else:
            count[s[r]]=1
        
        while (r-l+1) - max(count.values()) > k:
            count[s[l]]-=1
            l+=1
        streak=max(streak,r-l+1)
    
    return streak














    
    






















































