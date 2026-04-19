class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #IDEAS:
        #store the number of s1 in a list that have 26 smaller list to represent the number of occurance of each char in alphabet
        # store the number of s2 in another list that haev 26 smaller list 
        #use an val named matches to determine if 2 table matches or not (only compare n value at once (n respresent the len of s1))
        #for example: s1="abc" s2="baxyzabc" 
        #=> compare the occur list of"abc" with occur list of "bax"
        # then shift left ptr by 1 and compare occur list of "abc" and "axy"

        # matches if the number of occurance of 26 elements in the table are the same
        #else: not matches, shift the left ptr 

        if len(s1)>len(s2):
            return False
        
        s1_count=[0]*26
        s2_count=[0]*26

        #check "abc" with "lec" (in "lecabee") (when l=0 and r=len(s1)-1=2)
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord("a")]+=1
            s2_count[ord(s2[i])-ord("a")]+=1
        
        if s1_count==s2_count:
            return True
        
        #check "abc" with "eca", "cab", "abe", "bee"
        l=0
        for r in range(len(s1),len(s2),1): #start with eca 
            s2_count[ord(s2[r])-ord('a')]+=1 #move right ptr by 1 => r_ptr is at idx 3 (char "a") => add it to the occurance count
            s2_count[ord(s2[l])-ord('a')]-=1 #move left ptr by 1 => l_ptr is at idx 1 (char "e") => remove the old char occurance in s2_count

            if s2_count==s1_count:
                return True
            
            l+=1
        
        return False








"""
 ideas:
- since a permutation of s1 must have the same number of char as s1 => we gonna use FIXED-SIZE SLIDING WINDOW 
- we wanna check if the permutation of s1 is in s2 or not => we check by comparing the char occurance of s1 with the window in s2 => create 2 array to track the occrurance of s1 and s2 substring
- if they match => valid
"""
"""

    def permutation_string(s1,s2):
        if len(s1)>len(s2):
            return False
        
        s1_count=[0]*26
        s2_count=[0]*26

        #check "abc" with "lec" (in "lecabee") (when l=0 and r=len(s1)-1=2)
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord("a")]+=1
            s2_count[ord(s2[i])-ord("a")]+=1
        
        if s1_count==s2_count:
            return True
        
        #check "abc" with "eca", "cab", "abe", "bee"
        l=0
        for r in range(len(s1),len(s2),1): #start with eca 
            s2_count[ord(s[r])-ord('a')]+=1 #move right ptr by 1 => r_ptr is at idx 3 (char "a") => add it to the occurance count
            s2_count[ord(s[l])-ord('a')]-=1 #move left ptr by 1 => l_ptr is at idx 1 (char "e") => remove the old char occurance in s2_count

            if s2_count==s1_count:
                return True
            
            l+=1
        
        return False
      """      
    





    













































