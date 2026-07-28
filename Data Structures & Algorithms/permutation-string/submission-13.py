class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l = 0
        
        for r in range(len(s1)-1, len(s2)):
            s_2 = s2[l:r+1]
            if self.is_permutation(s1, s_2) == True:
                return True
            l+=1
        
        return False
    








    def is_permutation(self, s1, s2):
        if len(s1) != len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s2)):
            s1_count[ord(s1[i]) - ord('a')] +=1
            s2_count[ord(s2[i]) - ord('a')] +=1
        
        if s1_count == s2_count:
            return True
        return False


        