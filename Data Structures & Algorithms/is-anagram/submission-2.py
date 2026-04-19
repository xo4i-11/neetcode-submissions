class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        list_1=[]
        list_2=[]
        
        for i in range(0,len(s)):
            list_1.append(s[i])
            list_2.append(t[i])
        
        for j in list_1:
            if(j in list_2):
                list_2.remove(j)

        if(list_2==[]):
            return True

        return False