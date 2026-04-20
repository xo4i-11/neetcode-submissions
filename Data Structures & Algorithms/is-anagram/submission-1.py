class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bool =True;
        for i in range(0,len(s)):
            if(s[i] in t and len(s)==len(t)):
                bool=True
            else:
                return False
                
        return bool