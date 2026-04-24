class Solution:
    def isAnagram(self, s: str, t: str) -> bool: #we can use hashmap
        if(len(s)!=len(t)):
            return False

        count_s=[0]*26
        count_t=[0]*26
        
        for i in range (len(s)):
            count_s[ord(s[i])-ord("a")]+=1
            count_t[ord(t[i])-ord("a")]+=1
        
        if(count_s==count_t):
            return True
        return False

        

        
# i a list that contain the number of occurance of every char in s and t and compare
    
"""
IDEAS:
if the 2 length not equal => false

create 2 lists with 26 slots (for each), each slot have the element 0, to represent the number of occurance of every character 

loop through every char in s and t:
we gonna track the occurance of char in both string and put it inside the list 

afterwards, we compare

IMPLEMENTATION:
    def valid_ana(s,t):
        if len(s)!=len(t):
            return False

        count_s=[0]*26
        count_t=[0]*26

        for i in range(len(s)):
            count_s[ord(s[i])-ord("a")]+=1
            count_t[ord(t[i])-ord("a")]+=1
        
        return count_s==count_t

"""




def valid_anagram(s):
    if len(s)!=len(t):
        return False
    
    count_s=[0]*26
    count_s=[0]*26

    for i in range(len(s)):
        count_s[ord(s[i])-ord('a')]+=1
        count_t[ord(t[i])-ord('a')]+=1
    
    if count_s != count_t:
        return False
    return True
















































