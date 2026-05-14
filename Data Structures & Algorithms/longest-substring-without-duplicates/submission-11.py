class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0

        seen=set()
        count=0
        
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                count=max(count,len(seen))
                r+=1
            
            else:
                seen.remove(s[l])
                l+=1
        
        return count




            

        
        