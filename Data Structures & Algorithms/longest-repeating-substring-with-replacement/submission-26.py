class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #
        if len(s) == 0:
            return 0
        
        l=0
        streak=0
        count={}

        for r in range(len(s)):
            #track the most occurred char 
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            

            window_length = r-l+1
            max_occurance = max(count.values())

            # if the less occured char exceed k, we move the left ptr
            while window_length - max_occurance > k:
                count[s[l]]-=1
                l+=1
                window_length = r-l+1

            streak=max(streak, window_length )
        
        return streak





    

    """ 
    idea:
        - keep track of the most occurance char.
        - when exceed k, move the left ptr by 1



    """
        