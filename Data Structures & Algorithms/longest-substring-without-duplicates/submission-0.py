class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #find the length of longest string
        #no duplicate
        #example: "zxyxyz"
        #
        #l=0, r=0
        #r 0-> len s
        # xzyzxyz
        # r = 3
        #l=0 -> set{x,z,y}

        
        l=0
        r=0

        seen=set()
        max_count=0 
        track=0
        while l<=r and r<len(s):
            if (l<= r and (s[r] not in seen)):
                seen.add(s[r])
                track+=1
                max_count=max(max_count,track)
                r+=1

            elif(l<= r and (s[r] in seen)):
                seen=set()
                track=0
                while(s[l] != s[r]):
                    l+=1
                l+=1
                r=l
        
        return max_count
                





        

