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
        #if not: update the hashmap by: hashmap[s[l]]-=1,  l+=1  

        l=0
        longest=0
        hashmap={}
        max_occurance=0

        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]]=1

            max_occurance=max(max_occurance,hashmap[s[r]])


            if r-l+1 -max_occurance>k:
                hashmap[s[l]]-=1
                l+=1
            
            longest=max(longest,r-l+1)

        return longest

        


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









#IDEAS:
"""
we gonna do sliding window 
l=0, r run from 0-> len(s)-1

we gonna track the occurance of the elem that was being loop thrugh 1 by 1

if every thing work normal, just track the max substring
if the number of changing char exceed k => we need to move left ptr

"""

def longest_char_replace(s,k):
    longest=0
    l=0
    hashmap={}

    for r in range(len(s)):
        if s[r] in hashmap:
            hashmap[s[r]]+=1
        else:
            hashmap[s[r]]=1
        
        if (r-l+1) - max(hashmap.values())>k:
            hashmap[s[l]]-=1
            l+=1
        
        longest=max(longest,r-l+1)
    return longest
    

            







"""
ideas:
string: s
int: k (maximum number of replacement)

return the longest substring



i was thinking of using a sliding window
l=0, r= 0-> len(s)-1

the window will keep extend until we cannot replace the character
we will use the hashmap to store the occurance of the number every time we loop through

# if r=2 and the current window =XXY
we would need to replace Y with X
we would check if hashmap[X] - hashmap[Y] > k or not
=> max(hashmap.values()) - hashmap[y] >=k


"""

def longest_repeating(s,k):
    l=0
    longest=0
    hashmap={}
    max_occurance=0

    for r in range(len(s)):
        if s[r] in hashmap:
            hashmap[s[r]]+=1
        else:
            hashmap[s[r]]=1

        max_occurance=max(max_occurance,hashmap[s[r]])


        if r-l+1 -max_occurance>k:
            hashmap[s[l]]-=1
            l+=1
        
        longest=max(longest,r-l+1)

    return longest
        

    
















































