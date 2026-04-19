class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #IDEAS:
        #store the number of s1 in a list that have 26 smaller list to represent the number of occurance of each char in alphabet
        # store the number of s2 in another list that haev 26 smaller list 
        #use an val named matches to determine if 2 table matches or not (only compare n value at once (n respresent the len of s1))
        #for example: s1="abc" s2="baxyzabc" 
        #=> compare the occur list of"abc" with occur list of "bax"
        # then shift left ptr by 1 and compare occur list of "abc" and "axz"

        # matches if the number of occurance of 26 elements in the table are the same
        #else: not matches, shift the left ptr 

        if(len(s1)>len(s2)):
            return False
        
        s1Count=[0]*26
        s2Count=[0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord("a")]+=1
            s2Count[ord(s2[i])-ord("a")]+=1
        
        matches=0
        for i in range(26):
            if(s1Count[i]== s2Count[i]):
                matches+=1

        l=0
        for r in range(len(s1), len(s2)):
            if matches==26:
                return True
            
            index=ord(s2[r])- ord('a')
            s2Count[index]+=1 #shift the right ptr
            if s1Count[index]==s2Count[index]: #If it just became equal, we gain a match.
                matches+=1
            elif s1Count[index]+1== s2Count[index]:#If it was equal before but now not, we lose a match.
                matches-=1

            index=ord(s2[l])- ord('a')
            s2Count[index]-=1 #remove the left ptr
            if s1Count[index]==s2Count[index]: 
                matches+=1
            elif s1Count[index]-1== s2Count[index]: 
                matches-=1
            l+=1

        return matches==26

