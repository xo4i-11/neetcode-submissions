class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()
        res = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
                
        return res

        """
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
        
        """




    




















































        

