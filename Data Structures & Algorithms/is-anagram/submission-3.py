class Solution:
    def isAnagram(self, s: str, t: str) -> bool: #we can use hashmap
        if(len(s)!=len(t)):
            return False
        
        return sorted(s)==sorted(t) #make a list of character in alphabet order and compare