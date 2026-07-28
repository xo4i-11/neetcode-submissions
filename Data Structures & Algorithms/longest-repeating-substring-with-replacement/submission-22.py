class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #
        if len(s) == 0:
            return 0
        
        l=0
        streak=0
        count={}

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            
            if (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            streak=max(streak,r-l+1)
        
        return streak





    

    """ 
    idea:
        - keep track of the most occurance char.
        - when exceed k, move the left ptr by 1



    """
        